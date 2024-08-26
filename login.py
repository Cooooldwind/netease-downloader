import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QUrl, Signal, Slot
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtNetwork import QNetworkCookie


class LoginSubWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)
        self.page = MyWebEnginePage(self.web_view)
        self.web_view.setPage(self.page)
        self.page.cookieSignal.connect(self.handleCookie)
        self.web_view.load(QUrl("https://music.163.com/#/login/"))
        self.cookie_value = None
        self.setWindowTitle("浏览器模拟登录 - 不推荐使用密码登录/第三方 (QQ、微信) 暂时无法登录")
        
    def handleCookie(self, value):
        self.cookie_value = value
        print(value)
        self.destroy()
        return value


class MyWebEnginePage(QWebEnginePage):
    cookieSignal = Signal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile().cookieStore().deleteAllCookies()
        self.profile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        self.cookies = {}

    def onCookieAdd(self, cookie: QNetworkCookie):
        name = cookie.name().data().decode("utf-8")
        value = cookie.value().data().decode("utf-8")
        self.cookies[name] = value
        if name == "MUSIC_U":
            # 发出信号并传递 value 值
            self.cookieSignal.emit(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginSubWindow()
    window.show()
    sys.exit(app.exec())