from PySide6.QtCore import Slot, Signal, QObject
from typing import Dict

from module.search_result import SearchResult


class SearchController(QObject):
    edit_signal = Signal(dict)

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.module = SearchResult(self)
        self.module.search_signal.connect(self.add)
    
    def get(self, key, mode, search_type = "song"):
        self.module.set_attribute(key, mode, search_type)
        self.module.get()

    def add(self, result: Dict):
        self.edit_signal.emit(result)