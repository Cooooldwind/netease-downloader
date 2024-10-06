from PySide6.QtCore import Slot, Signal, QObject
from typing import Dict, List

from model import ApplicationModel
from view import MainWindow
from view.frame_widget import MusicCardWidget

class Application(QObject):
    def __init__(self):
        super().__init__()
        self.application_model = ApplicationModel(self)
        self.mainwindow_view = MainWindow()
        self.mainwindow_view.search_widget.ui.SearchKeyLineEdit.returnPressed.connect(self.search)
        self.mainwindow_view.search_widget.ui.SearchKeyLineEdit.searchSignal.connect(self.search)
        self.mainwindow_view.home_widget.ui.CookieLineEdit.returnPressed.connect(self.update_cookies)
        self.mainwindow_view.home_widget.ui.LoginButton.clicked.connect(self.update_cookies)

    def update_cookies(self):
        key = self.mainwindow_view.home_widget.ui.CookieLineEdit.text()
        self.application_model.config.cookies = {"MUSIC_U": key}
        self.application_model.config.add_cookies()
        self.mainwindow_view.home_widget.ui.CookieLineEdit.clear()

    def search(self):
        key = self.mainwindow_view.search_widget.ui.SearchKeyLineEdit.text()
        mode_index = (
            self.mainwindow_view.search_widget.ui.SearchTypeComboBox.currentIndex()
        )
        mode_list = ["song", "playlist", "search_song", "search_playlist"]
        current_mode = mode_list[mode_index]
        self.application_model.start_search_instance(key=key, search_mode=current_mode)
        self.application_model.search_model.result_signal.connect(self.update_search_result_table)
        self.mainwindow_view.search_widget.ui.SearchResultLabel.setText("正在搜索...")
    
    def update_search_result_table(self, result_dict: Dict):
        if result_dict["mode"] == "initialize":
            text = ""
            if result_dict["search_mode"] == "playlist":
                text = f"搜索到歌单:{result_dict["title"]}, 由 {result_dict["creator"]} 创建, 共 {result_dict["tot"]} 首。"
            elif result_dict["search_mode"] == "search_song":
                text = f"搜索到 {result_dict["title"]} 相关歌曲共 {result_dict["tot"]} 首。"
            elif result_dict["search_mode"] == "search_playlist":
                text = f"搜索到 {result_dict["title"]} 相关歌单共 {result_dict["tot"]} 个。"
            else:
                text = f"搜索到 {result_dict["title"]}。"
            self.mainwindow_view.search_widget.ui.SearchResultLabel.setText(text)
            self.mainwindow_view.search_widget.ui.SearchResultTable.setRowCount(result_dict["tot"])
            self.mainwindow_view.search_widget.ui.ProgressBar.setRange(0, result_dict["tot"])
            self.mainwindow_view.search_widget.ui.ProgressBar.setValue(0)
            self.mainwindow_view.search_widget.ui.ProgressBar.setHidden(False)
            for i in range(result_dict["tot"]):
                self.mainwindow_view.search_widget.ui.SearchResultTable.setRowHeight(i, 80)
                self.mainwindow_view.search_widget.ui.SearchResultTable.setRowHidden(i, True)
        elif result_dict["mode"] == "edit":
            if result_dict["item"] == "music":
                widget = MusicCardWidget(
                    coverbytes=result_dict["cover"],
                    title=result_dict["title"],
                    artist_str=result_dict["artist"],
                    album=result_dict["album"],
                    index=result_dict["index"]+1,
                    sub_title=result_dict["sub_title"],
                    trans_title=result_dict["trans_title"],
                    parent=self.mainwindow_view.search_widget.ui.SearchResultTable,
                )
                self.mainwindow_view.search_widget.ui.SearchResultTable.setCellWidget(result_dict["index"], 0, widget)
                self.mainwindow_view.search_widget.ui.SearchResultTable.setRowHidden(result_dict["index"], False)
                text = ""
                if result_dict["search_mode"] == "playlist":
                    text = f"搜索到歌单:{result_dict["playlist_title"]}, 由 {result_dict["creator"]} 创建, 共 {result_dict["tot"]} 首, 已加载 {result_dict["index"]+1}/{result_dict["tot"]} 首。"
                elif result_dict["search_mode"] == "search_song":
                    text = f"搜索到 {result_dict["key"]} 相关歌曲共 {result_dict["tot"]} 首, 已加载 {result_dict["index"]+1}/{result_dict["tot"]} 首。"
                self.mainwindow_view.search_widget.ui.SearchResultLabel.setText(text)
                self.mainwindow_view.search_widget.ui.ProgressBar.setValue(result_dict["index"]+1)
                