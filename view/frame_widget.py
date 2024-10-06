from PySide6.QtWidgets import QFrame, QHeaderView
from PySide6.QtCore import QObject
from PySide6.QtGui import QImage

from qfluentwidgets import FluentIcon as FIF

from typing import Dict, Union

from view.home_frame import Ui_Home
from view.download_list_frame import Ui_DownloadList
from view.search_frame import Ui_Search
from view.music_card_frame import Ui_MusicCardFrame


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
    def edit_table(self, result: Dict):
        pass           


class MusicCardWidget(QFrame):
    def __init__(
        self,
        coverbytes: bytes, title: str, artist_str: str, album: str,
        sub_title: str, trans_title: str, index: int, parent: QObject | None = ...,
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
