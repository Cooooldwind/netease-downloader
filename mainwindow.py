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

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browserLoginButton.clicked.connect(self.login)
        self.ui.loginLineEdit.returnPressed.connect(self.set_cookie)
        self.ui.loginButton.clicked.connect(self.set_cookie)
        self.encode_session = EncodeSession()
        self.cookie = {}

    def set_cookie(self):
        self.cookie = {"MUSIC_U":self.ui.loginLineEdit.text()}
        self.encode_session.set_cookies(self.cookie)
        self.ui.loginLineEdit.clear()
        self.ui.loginLabel.setText(QApplication.translate("","登录成功！",""))

    def login(self):
        login_window = LoginSubWindow()
        login_window.show()
        event_loop = QEventLoop()
        login_window.destroyed.connect(event_loop.quit)
        event_loop.exec()
        if login_window.destroyed:
            self.cookie = {"MUSIC_U":login_window.cookie_value}
            self.encode_session.set_cookies(self.cookie)
        self.ui.loginLabel.setText(QApplication.translate("","登录成功！",""))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    refresh_thread = RefreshThread(widget)
    refresh_thread.start()
    widget.show()
    sys.exit(app.exec())
