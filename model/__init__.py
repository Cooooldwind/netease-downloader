from PySide6.QtCore import QObject

from model.config import Config
from model.search_model import SearchModel
from model.global_args import SEARCH_MODE


class ApplicationModel(QObject):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.config = Config()
        self.search_model: SearchModel = None

    def start_search_instance(self, key: str, search_mode: SEARCH_MODE):
        self.config.add_cookies()
        self.search_model = SearchModel(
            encode_session=self.config.encode_session,
            key=key,
            search_mode=search_mode,
            parent=self,
        )
        self.search_model.start()
    
