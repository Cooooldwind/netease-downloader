from PySide6.QtCore import Slot, Signal, QObject

from module.search_result import SearchResult


class SearchController(QObject):
    result_slot = Slot(dict)
    run_slot = Slot(dict)
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.module = SearchResult(self)
        self.module.search_signal.connect(self.result_slot)
        