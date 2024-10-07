from PySide6.QtWidgets import QFrame, QHeaderView
from PySide6.QtCore import QObject
from PySide6.QtGui import QImage

from qfluentwidgets import FluentIcon as FIF

from typing import Dict

from view.home_frame import Ui_Home
from view.download_list_frame import Ui_DownloadList
from view.search_frame import Ui_Search
from view.music_card_frame import Ui_MusicCardFrame


def result_text(result_dict: Dict) -> str:
    text = ""
    if result_dict["mode"] == "initialize":
        # 搜索结果提示语的编辑
        if result_dict["search_mode"] == "playlist":
            text = f"搜索到歌单:{result_dict["title"]}, 由 {result_dict["creator"]} 创建, 共 {result_dict["tot"]} 首。"
        elif result_dict["search_mode"] == "search_song":
            text = f"搜索到 {result_dict["title"]} 相关歌曲共 {result_dict["tot"]} 首。"
        elif result_dict["search_mode"] == "search_playlist":
            text = f"搜索到 {result_dict["title"]} 相关歌单共 {result_dict["tot"]} 个。"
        else:
            text = f"搜索到 {result_dict["title"]}。"
    elif result_dict["mode"] == "edit":
        if result_dict["search_mode"] == "playlist":
            text = f"搜索到歌单:{result_dict["playlist_title"]}, 由 {result_dict["creator"]} 创建, 共 {result_dict["tot"]} 首, 已加载 {result_dict["index"]+1}/{result_dict["tot"]} 首。"
        elif result_dict["search_mode"] == "search_song":
            text = f"搜索到 {result_dict["key"]} 相关歌曲共 {result_dict["tot"]} 首, 已加载 {result_dict["index"]+1}/{result_dict["tot"]} 首。"
    elif result_dict["mode"] == "ending":
        # 搜索结果提示语的编辑
        if result_dict["search_mode"] == "playlist":
            text = f"搜索到歌单:{result_dict["title"]}, 由 {result_dict["creator"]} 创建, 共 {result_dict["tot"]} 首。"
        elif result_dict["search_mode"] == "search_song":
            text = f"搜索到 {result_dict["title"]} 相关歌曲共 {result_dict["tot"]} 首。"
        elif result_dict["search_mode"] == "search_playlist":
            text = f"搜索到 {result_dict["title"]} 相关歌单共 {result_dict["tot"]} 个。"
        else:
            text = f"搜索到 {result_dict["title"]}。"
    return text

class HomeWidget(QFrame):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)


class DownloadListWidget(QFrame):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_DownloadList()
        self.ui.setupUi(self)


class SearchWidget(QFrame):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_Search()
        self.ui.setupUi(self)
        # 初始化
        self.ui.SearchResultTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.SearchResultTable.setBorderVisible(True)
        self.ui.SearchResultTable.setBorderRadius(8)
        self.ui.ProgressBar.setValue(0)
        self.ui.ProgressBar.setHidden(True)
    def edit_result_ui(self, result_dict: Dict):
        # 接受初始化信号 在获得了一个大概的数据之后执行
        if result_dict["mode"] == "initialize":
            # 搜索结果提示语的编辑
            self.ui.SearchResultLabel.setText(result_text(result_dict))
            # 初始化设置这个不是表格的表格
            self.ui.SearchResultTable.setRowCount(result_dict["tot"])
            for i in range(result_dict["tot"]):
                self.ui.SearchResultTable.setRowHeight(i, 80)
                self.ui.SearchResultTable.setRowHidden(i, True)
            # 初始化设置进度条
            self.ui.ProgressBar.setRange(0, result_dict["tot"])
            self.ui.ProgressBar.setValue(0)
            self.ui.ProgressBar.setHidden(False)
        # 详细信息编辑信号
        elif result_dict["mode"] == "edit":
            # 在假装是列表的表格里面加一首歌
            if result_dict["item"] == "music":
                widget = MusicCardWidget(
                    coverbytes=result_dict["cover"],
                    title=result_dict["title"],
                    artist_str=result_dict["artist"],
                    album=result_dict["album"],
                    index=result_dict["index"]+1,
                    sub_title=result_dict["sub_title"],
                    trans_title=result_dict["trans_title"],
                    parent=self.ui.SearchResultTable,
                )
                self.ui.SearchResultTable.setCellWidget(result_dict["index"], 0, widget)
                self.ui.SearchResultTable.setRowHidden(result_dict["index"], False)
            # 搜索结果提示语的编辑
            self.ui.SearchResultLabel.setText(result_text(result_dict))
            # 进度条编辑
            self.ui.ProgressBar.setValue(result_dict["index"] + 1)
        # 结束编辑信号
        elif result_dict["mode"] == "ending":
            # 搜索结果提示语的编辑
            self.ui.SearchResultLabel.setText(result_text(result_dict))
            # 设置进度条
            self.ui.ProgressBar.setHidden(False)



class MusicCardWidget(QFrame):
    def __init__(
        self,
        title: str, artist_str: str, album: str,sub_title: str,
        trans_title: str, index: int, coverbytes: bytes = None,
        parent: QObject | None = ...,
    ) -> None:
        super().__init__(parent)
        self.ui = Ui_MusicCardFrame()
        self.ui.setupUi(self)
        # 样式
        self.ui.CoverLabel.setBorderRadius(4, 4, 4, 4)
        self.ui.ArtistIcon.setPixmap(FIF.PEOPLE.icon().pixmap(14))
        self.ui.AlbumIcon.setPixmap(FIF.ALBUM.icon().pixmap(14))
        self.ui.DownloadButton.setIcon(FIF.DOWNLOAD)
        # 编辑
        if coverbytes != None:
            cover = QImage()
            cover.loadFromData(coverbytes)
        self.ui.Index.setText(str(index))
        self.ui.CoverLabel.setImage(cover)
        self.ui.Title.setText(title)
        self.ui.Artist.setText(artist_str)
        self.ui.Album.setText(album)
        self.ui.Subtitle.setText(sub_title)
        trans_title = "(" + trans_title + ")" if trans_title != "" else ""
        self.ui.TransTitle.setText(trans_title)
