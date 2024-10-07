from PySide6.QtCore import QObject
from typing import Dict, List

from model import ApplicationModel
from view import MainWindow

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
        self.application_model.search_model.result_signal.connect(self.mainwindow_view.search_widget.edit_result_ui)
        self.mainwindow_view.search_widget.ui.SearchResultLabel.setText("正在搜索...")

                