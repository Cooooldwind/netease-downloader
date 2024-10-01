import sys
from PySide6.QtWidgets import QFrame, QHBoxLayout, QApplication, QVBoxLayout, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Slot, Signal, Qt
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
from typing import Dict

# 内部调用
from view.frame_widget import HomeWidget, DownloadListWidget, SearchWidget
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

        # 信号
        self.search_widget.ui.SearchPushButton.clicked.connect(self.search)

        # 初始化
        self.search_widget.ui.SearchResultTable.setBorderVisible(True)
        self.search_widget.ui.SearchResultTable.setBorderRadius(8)

    def search(self):
        key = self.search_widget.ui.SearchKeyLineEdit.text()
        self.search_controller.get(key, "playlist", "playlist")
        self.search_controller.edit_signal.connect(self.edit_search_result)

    def edit_search_result(self, result: Dict):
        if result["mode"] == "initialize":
            self.search_widget.ui.SearchResultTable.setRowCount(result["cnt"])
            for i in range(result["cnt"]):
                self.search_widget.ui.SearchResultTable.setRowHidden(i, True)
            self.search_widget.ui.SearchResultLabel.setText(f"搜索到 {result["playlist_title"]}，由 {result["playlist_creator"]} 创建，共 {result["cnt"]} 首歌曲。")
        elif result["mode"] == "edit_table":
            self.search_widget.ui.SearchResultTable.setItem(result["cnt"],0,QTableWidgetItem(result["title"]))
            self.search_widget.ui.SearchResultTable.setItem(result["cnt"],1,QTableWidgetItem(result["artist"]))
            self.search_widget.ui.SearchResultTable.setItem(result["cnt"],2,QTableWidgetItem(result["album"]))
            self.search_widget.ui.SearchResultTable.setRowHidden(result["cnt"], False)

    def initNavigation(self):
        self.addSubInterface(self.home_widget, FIF.HOME, "主页")
        self.addSubInterface(self.search_widget, FIF.SEARCH, "搜索")
        self.addSubInterface(self.download_list_widget, FIF.LIBRARY, "下载列表")
        # self.addSubInterface()

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowTitle("NeteaseDownloader")


