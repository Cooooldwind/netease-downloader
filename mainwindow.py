# This Python file uses the following encoding: utf-8
import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, QEventLoop, Signal, Slot
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
from music_widget import Ui_musicWidget

# for cover picture
from PySide6.QtGui import QPixmap, QImage
from class163.origin_file import OriginFile

# temp
from class163 import Music, Playlist
from pprint import pprint
from class163.music import artist_join
import requests
import global_bin


class EventThread(QThread):
    mode1_signal = Signal(dict)
    def __init__(self):
        super(EventThread, self).__init__()
        self.playlist = None
        self.song = None
        self.search_result = None
        self.mode = None
        self.text = None
        self.result = None
        self.encode_session: EncodeSession = None
        self.source: Playlist = None

    def run(self):
        if self.mode == 1:
            self.source = Playlist(self.text)
            self.source.get_detail(session=self.encode_session)
            self.result = self.source.info_dict()
            result = dict(self.result)
            sorted = {}
            sorted.update({"row": int(result["track_count"])})
            for i in range(int(result["track_count"])):
                try:
                    data = bytes()
                    now = result["track_info"][i]
                    title, artist = now["title"], artist_join(now["artist"],"/")
                    cover_url = f"{self.source.track[i].detail_info_raw["al"]["picUrl"]}?param=48y48"
                    of = OriginFile(cover_url)
                    of.begin_download()
                    data = of.get_data()
                except requests.HTTPError:
                    pass
                except Exception as e:
                    print(e)
                    pass
                finally:
                    sorted.update({
                        "title": title,
                        "artist": artist,
                        "data": data,
                        "index": i,
                    })
                    self.mode1_signal.emit(sorted)
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
        self.event_thread.finished.connect(self.search_end)
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
        # self.ui.resultTableWidget.setBorderVisible(True)
        # self.ui.resultTableWidget.setBorderRadius(8)
        self.cookie = {}

    def search(self):
        mode = self.search_mode
        if mode not in [1]:
            return None
        else:
            self.event_thread.mode = mode
            self.event_thread.text = self.ui.searchLineEdit.text()
            self.event_thread.encode_session = self.encode_session
            self.event_thread.mode1_signal.connect(self.update_result_table)
            self.event_thread.start()
            self.ui.infoLabel.setText("正在获取歌单......")
    def search_end(self):
        self.ui.infoLabel.setText(f"歌单 \"{self.event_thread.result["title"]}\" 获取完成,，共 {str(self.event_thread.result["track_count"])} 首歌曲。")
        self.update()

    @Slot(dict)
    def update_result_table(self, result):
        if self.search_mode == 1:
            result = dict(result)
            new = Ui_musicWidget()
            widget = QWidget()
            new.setupUi(widget)
            new.titleLabel.setText(result["title"])
            new.artistLabel.setText(result["artist"])
            img = QImage.fromData(result["data"] if result["data"] != b"" else global_bin.DEFAULT_COVER)
            new.coverLabel.setImage(img)
            new.coverLabel.scaledToWidth(48)
            new.coverLabel.scaledToHeight(48)
            new.coverLabel.setBorderRadius(8,8,8,8)
            self.ui.resultTableWidget.setRowCount(int(result["index"]))
            self.ui.resultTableWidget.setColumnWidth(0, 400)
            self.ui.resultTableWidget.setRowHeight(result["index"], 64)
            self.ui.resultTableWidget.setCellWidget(int(result["index"]), 0, widget)
            self.ui.infoLabel.setText(f"正在加载歌单... {result["index"]}/{result["row"]}")
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
    widget.show()
    sys.exit(app.exec())
