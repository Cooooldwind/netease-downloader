import sys
from PySide6.QtWidgets import QFrame, QHBoxLayout, QApplication, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (
    NavigationItemPosition,
    MessageBox,
    setTheme,
    Theme,
    MSFluentWindow,
    NavigationAvatarWidget,
    qrouter,
    SubtitleLabel,
    setFont,
    FluentIcon,
)
from qfluentwidgets import FluentIcon as FIF

# 内部调用
from frame_widget import HomeWidget, DownloadListWidget, SearchWidget
from controller import SearchController


class Window(MSFluentWindow):
    def __init__(self):
        super().__init__()
        # 创建控制器
        self.search_controller = SearchController(self)

        # 窗口
        self.home_widget = HomeWidget(self)
        self.download_list_widget = DownloadListWidget(self)
        self.search_widget = SearchWidget(self)
        self.initNavigation()
        self.initWindow()


    def initNavigation(self):
        self.addSubInterface(self.home_widget, FIF.HOME, "主页")
        self.addSubInterface(self.search_widget, FIF.SEARCH, "搜索")
        self.addSubInterface(self.download_list_widget, FIF.LIBRARY, "下载列表")
        # self.addSubInterface()

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowTitle("NeteaseDownloader")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
