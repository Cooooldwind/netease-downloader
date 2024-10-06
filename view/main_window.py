import sys
from PySide6.QtWidgets import QFrame, QHBoxLayout, QApplication, QVBoxLayout, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Slot, Signal, Qt
from qfluentwidgets import (
    MSFluentWindow,
)
from qfluentwidgets import FluentIcon as FIF
from typing import Dict

# 内部调用
from view.frame_widget import HomeWidget, DownloadListWidget, SearchWidget, MusicCardWidget
from controller import SearchController

from module.config import Config


class Window(MSFluentWindow):

    def __init__(self):
        super().__init__()
        # 创建控制器
        self.search_controller = SearchController(self)

        # 配置文件
        self.config = Config()

        # 窗口
        self.home_widget = HomeWidget(self)
        self.download_list_widget = DownloadListWidget(self)
        self.search_widget = SearchWidget(self)
        self.initNavigation()
        self.initWindow()

        # 信号
        self.search_widget.ui.SearchKeyLineEdit.returnPressed.connect(self.search)
        self.search_widget.ui.SearchKeyLineEdit.searchSignal.connect(self.search)
        self.search_widget.ui.SearchTypeComboBox.currentIndexChanged.connect(self.search_mode_change)

        # 初始化
        self.search_widget.ui.SearchResultTable.setBorderVisible(True)
        self.search_widget.ui.SearchResultTable.setBorderRadius(8)
        self.search_widget.ui.ProgressBar.setValue(0)
        self.search_widget.ui.ProgressBar.setHidden(True)

    def search_mode_change(self):
        tmp = self.search_widget.ui.SearchTypeComboBox.currentIndex() 
        self.config.search_mode = (
            "song" if tmp == 0 else (
                "playlist" if tmp == 1 else (
                    "search_song" if tmp == 2 else "search_playlist"
                )
            )
        )
        

    def search(self):
        key = self.search_widget.ui.SearchKeyLineEdit.text()
        self.search_controller.edit_signal.connect(self.edit_search_result)
        self.search_controller.get(key, self.config.search_mode, "playlist")
        self.search_widget.ui.SearchResultLabel.setText("正在搜索......")

    def edit_search_result(self, result: Dict):
        if result["mode"] == "initialize":
            self.search_widget.ui.SearchResultTable.setRowCount(result["cnt"])
            self.search_widget.ui.SearchResultTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
            self.search_widget.ui.ProgressBar.setRange(0, result["cnt"])
            for i in range(result["cnt"]):
                self.search_widget.ui.SearchResultTable.setRowHidden(i, True)
                self.search_widget.ui.SearchResultTable.setRowHeight(i, 80)
            self.search_widget.ui.SearchResultLabel.setText(f"搜索到 {result["playlist_title"]}，由 {result["playlist_creator"]} 创建，共 {result["cnt"]} 首歌曲。")
        elif result["mode"] == "edit_table":
            widget_tmp = MusicCardWidget(
                coverbytes=result["cover"],
                title=result["title"],
                artist_str=result["artist"],
                album=result["album"],
                sub_title=result["sub_title"],
                trans_title=result["trans_title"],
                parent=self.search_widget.ui.SearchResultTable
            )
            self.search_widget.ui.SearchResultTable.setCellWidget(result["cnt"],0,widget_tmp)
            self.search_widget.ui.SearchResultTable.setRowHidden(result["cnt"], False)
            self.search_widget.ui.ProgressBar.setHidden(False)
            self.search_widget.ui.ProgressBar.setValue(result["cnt"])
            self.search_widget.ui.SearchResultLabel.setText(f"搜索到 {result["playlist_title"]}，由 {result["playlist_creator"]} 创建，共 {result["tot_cnt"]} 首歌曲。已加载 {result["cnt"]}/{result["tot_cnt"]} 首。")
        elif result["mode"] == "ending":
            self.search_widget.ui.SearchResultLabel.setText(f"搜索到 {result["playlist_title"]}，由 {result["playlist_creator"]} 创建，共 {result["cnt"]} 首歌曲。全部加载完成。")
            self.search_widget.ui.ProgressBar.setHidden(True)

    def initNavigation(self):
        self.addSubInterface(self.home_widget, FIF.HOME, "主页")
        self.addSubInterface(self.search_widget, FIF.SEARCH, "搜索")
        self.addSubInterface(self.download_list_widget, FIF.LIBRARY, "下载列表")
        # self.addSubInterface()

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowTitle("NeteaseDownloader")


