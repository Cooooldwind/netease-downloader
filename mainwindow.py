# This Python file uses the following encoding: utf-8
import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, QEventLoop
from PySide6.QtWidgets import QApplication
from login import LoginSubWindow
from netease_encode_api import EncodeSession
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from typing import List, Dict


class RefreshThread(QThread):
    def __init__(self, window: QMainWindow):
        super().__init__()
        self.window = window

    def run(self):
        while True:
            self.window.update()
            time.sleep(0.05)


class Event:
    def __init__(self):
        self.playlist = None
        self.song = None
        self.search_result = None

    def get(self):
        pass


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
        self.search_mode = self.ui.searchComboBox.currentIndex()
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

    def search_mode_change(self):
        self.search_mode = self.ui.searchComboBox.currentIndex()
        print(self.search_mode)

    def set_level_standard(self):
        self.level = "standard"
        print(self.level)

    def set_level_higher(self):
        self.level = "higher"
        print(self.level)

    def set_level_exhigh(self):
        self.level = "exhigh"
        print(self.level)

    def set_level_lossless(self):
        self.level = "lossless"
        print(self.level)

    def status_update(self):
        self.basic_info, self.lyrics_add, self.album_cover, self.lyrics_download = (
            self.ui.basicInfoCheckBox.isChecked(),
            self.ui.lyricsAddCheckBox.isChecked(),
            self.ui.albumCoverCheckBox.isChecked(),
            self.ui.lyricsDownloadCheckBox.isChecked(),
        )
        print(self.basic_info, self.lyrics_add, self.album_cover, self.lyrics_download)

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
