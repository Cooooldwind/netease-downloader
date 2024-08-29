# This Python file uses the following encoding: utf-8
import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, QEventLoop
from PySide6.QtWidgets import *
from login import LoginSubWindow
from netease_encode_api import EncodeSession

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from typing import List, Dict
from music_frame import Ui_Frame

# for cover picture
from PySide6.QtGui import QPixmap, QImage
from class163.origin_file import OriginFile

# temp
from class163.playlist import Playlist
from pprint import pprint
from class163.music import artist_join


class RefreshThread(QThread):
    def __init__(self, window: QMainWindow):
        super().__init__()
        self.window = window

    def run(self):
        while True:
            self.window.update()
            time.sleep(0.05)


class EventThread(QThread):
    def __init__(self):
        super(EventThread, self).__init__()
        self.playlist = None
        self.song = None
        self.search_result = None
        self.mode = None
        self.text = None
        self.result = None
        self.encode_session: EncodeSession = None
        self.source = None

    def run(self):
        if self.mode == 1:
            self.source = Playlist(self.text)
            self.source.get_detail(session=self.encode_session)
            self.result = self.source.info_dict()
        return None


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browserLoginButton.clicked.connect(self.login)
        self.ui.loginLineEdit.returnPressed.connect(self.set_cookie)
        self.ui.loginButton.clicked.connect(self.set_cookie)
        self.encode_session = EncodeSession()
        self.basic_info, self.lyrics_add, self.album_cover, self.lyrics_download = (
            False,
            False,
            False,
            False,
        )
        self.level = None
        self.event_thread = EventThread()
        self.event_thread.finished.connect(self.update_result_table)
        self.search_mode = self.ui.searchComboBox.currentIndex()
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.searchLineEdit.returnPressed.connect(self.search)
        self.ui.searchComboBox.currentIndexChanged.connect(self.search_mode_change)
        self.ui.standardRadioButton.clicked.connect(self.set_level_standard)
        self.ui.higherRadioButton.clicked.connect(self.set_level_higher)
        self.ui.exhighRadioButton.clicked.connect(self.set_level_exhigh)
        self.ui.losslessRadioButton.clicked.connect(self.set_level_lossless)
        self.ui.basicInfoCheckBox.clicked.connect(self.status_update)
        self.ui.lyricsAddCheckBox.clicked.connect(self.status_update)
        self.ui.albumCoverCheckBox.clicked.connect(self.status_update)
        self.ui.lyricsDownloadCheckBox.clicked.connect(self.status_update)
        self.cookie = {}

    def search(self):
        mode = self.search_mode
        if mode not in [1]:
            return None
        else:
            self.event_thread.mode = mode
            self.event_thread.text = self.ui.searchLineEdit.text()
            self.event_thread.encode_session = self.encode_session
            self.event_thread.start()
            self.ui.infoLabel.setText("正在获取歌单......")
        """
        event_thread.start()
        while True:
            result = event_thread.result
            if result != None:
                event_thread.result = None
                break
            else: 
                self.update()
                time.sleep(0.05)
        """

    def update_result_table(self):
        result = self.event_thread.result
        if self.search_mode == 1:
            result = dict(result)
            self.ui.resultTableWidget.setRowCount(int(result["track_count"]))
            for i in range(int(result["track_count"])):
                self.ui.infoLabel.setText(f"正在加载歌单... {i}/{int(result["track_count"])}")
                self.update()
                now = result["track_info"][i]
                title, subtitle, artist = now["title"], now["subtitle"], artist_join(now["artist"],"/")
                new_frame = Ui_Frame()
                frame_widget = QWidget()
                new_frame.setupUi(frame_widget)
                new_frame.titleLabel.setText(title)
                new_frame.subtitleLabel.setText(subtitle)
                new_frame.aritstLabel.setText(artist)
                cover_url = f"{self.event_thread.source.track[i].detail_info_raw["al"]["picUrl"]}?param=60y60"
                of = OriginFile(cover_url)
                of.begin_download()
                data = of.get_data()
                img = QImage.fromData(data)
                pixmap = QPixmap.fromImage(img)
                new_frame.coverLabel.setPixmap(pixmap)
                self.ui.resultTableWidget.setCellWidget(i, 0, frame_widget)
                self.ui.resultTableWidget.setColumnWidth(0, 400)
                self.ui.resultTableWidget.setRowHeight(i, 80)
                self.update()
            self.ui.infoLabel.setText(f"歌单 \"{result["title"]}\" 获取完成,，共 {str(result["track_count"])} 首歌曲。")
            self.update()
        return None

    def search_mode_change(self):
        self.search_mode = self.ui.searchComboBox.currentIndex()

    def set_level_standard(self):
        self.level = "standard"

    def set_level_higher(self):
        self.level = "higher"

    def set_level_exhigh(self):
        self.level = "exhigh"

    def set_level_lossless(self):
        self.level = "lossless"

    def status_update(self):
        self.basic_info, self.lyrics_add, self.album_cover, self.lyrics_download = (
            self.ui.basicInfoCheckBox.isChecked(),
            self.ui.lyricsAddCheckBox.isChecked(),
            self.ui.albumCoverCheckBox.isChecked(),
            self.ui.lyricsDownloadCheckBox.isChecked(),
        )

    def set_cookie(self):
        self.cookie = {"MUSIC_U": self.ui.loginLineEdit.text()}
        self.encode_session.set_cookies(self.cookie)
        self.ui.loginLineEdit.clear()
        self.ui.loginLabel.setText(QApplication.translate("", "登录成功！", ""))

    def login(self):
        login_window = LoginSubWindow()
        login_window.show()
        event_loop = QEventLoop()
        login_window.destroyed.connect(event_loop.quit)
        event_loop.exec()
        if login_window.destroyed:
            self.cookie = {"MUSIC_U": login_window.cookie_value}
            self.encode_session.set_cookies(self.cookie)
        self.ui.loginLabel.setText(QApplication.translate("", "登录成功！", ""))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    refresh_thread = RefreshThread(widget)
    refresh_thread.start()
    widget.show()
    sys.exit(app.exec())
