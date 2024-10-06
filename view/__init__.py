import sys
from PySide6.QtCore import QObject
from PySide6.QtGui import QPixmap, QIcon

from qfluentwidgets import MSFluentWindow, setThemeColor, FluentIcon

from typing import Dict

# 内部调用
from view.frame_widget import HomeWidget, DownloadListWidget, SearchWidget


class MainWindow(MSFluentWindow):

    def __init__(self):
        super().__init__()
        # widgets
        self.home_widget = HomeWidget(self)
        self.download_list_widget = DownloadListWidget(self)
        self.search_widget = SearchWidget(self)
        self.icon = QIcon("resources/icon.png")
        self.initNavigation()
        self.initWindow()
    
    def initNavigation(self):
        self.addSubInterface(self.home_widget, FluentIcon.HOME, "主页")
        self.addSubInterface(self.search_widget, FluentIcon.SEARCH, "搜索")
        self.addSubInterface(self.download_list_widget, FluentIcon.LIBRARY, "下载列表")

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowTitle("NeteaseDownloader")
        self.setWindowIcon(self.icon)
        setThemeColor("#FD3D4A")


