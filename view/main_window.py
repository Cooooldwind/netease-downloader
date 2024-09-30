import sys
from PySide6.QtWidgets import QFrame, QHBoxLayout, QApplication, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, FluentIcon)
from qfluentwidgets import FluentIcon as FIF

# 内部调用
from home_frame import Ui_Home
from download_list_frame import Ui_DownloadList
from search_frame import Ui_Search

"""
class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignmentFlag.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))
"""


class HomeWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)

class DownloadListWidget(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.ui = Ui_DownloadList()
        self.ui.setupUi(self)

class SearchWidget(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.ui = Ui_Search()
        self.ui.setupUi(self)

class Window(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.home_widget = HomeWidget(parent=self)
        self.download_list_widget = DownloadListWidget(parent=self)
        self.search_widget = SearchWidget(parent=self)
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.home_widget, FIF.HOME, '主页')
        self.addSubInterface(self.search_widget, FIF.SEARCH, "搜索")
        self.addSubInterface(self.download_list_widget, FIF.LIBRARY, "下载列表")
        # self.addSubInterface()

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowTitle('NeteaseDownloader')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
