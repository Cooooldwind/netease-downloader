from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QObject

from home_frame import Ui_Home
from download_list_frame import Ui_DownloadList
from search_frame import Ui_Search


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
