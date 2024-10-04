from io import BytesIO

from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QObject
from PySide6.QtGui import QImage

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

class MusicCardWidget(QFrame):
    def __init__(self, coverbytes: bytes, title: str, artist_str: str, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_MusicCardFrame()
        self.ui.setupUi(self)
        # 编辑
        cover = QImage()
        cover.loadFromData(coverbytes)
        self.ui.CoverLabel.setImage(cover)
        self.ui.Title.setText(title)
        self.ui.Artist.setText(artist_str)
        # 样式
        self.ui.CoverLabel.setBorderRadius(4,4,4,4)        

