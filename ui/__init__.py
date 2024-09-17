# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.main_window import Ui_MainWindow

# pySide6
from PySide6.QtCore import Slot
from PySide6.QtGui import QImage

# netease_encode_api
from netease_encode_api import EncodeSession

# class163
from class163 import Music

# qfluentwidgets
import qfluentwidgets

# 私有类
from model.search_result import SearchResultModel
from controller.search_result import SearchResultController
from ui.music_frame import Ui_Frame
from global_args.global_bin import DEFAULT_COVER

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 属性啥的
        self.encode_session = EncodeSession()    
        self.level = None
        self.basic_info, self.lyrics_add, self.album_cover, self.lyrics_download = (
            False,
            False,
            False,
            False,
        )
        # 搜索相关控制器和模型
        self.search_model = SearchResultModel()
        self.search_controller = SearchResultController(self.search_model)
        # 信号
        self.ui.searchButton.clicked.connect(self.search)
        # 属性
        self.ui.resultTableWidget.setBorderVisible(True)
        self.ui.resultTableWidget.setBorderRadius(8)
        self.ui.resultTableWidget.setColumnWidth(0, 120)
        self.ui.resultTableWidget.setColumnWidth(1, 400)
        self.ui.resultTableWidget.setColumnWidth(2, 80)
        # 杂项
        qfluentwidgets.setThemeColor("#fc3d49")

    def search(self):
        self.search_controller.encode_session = self.encode_session
        self.search_controller.update_init_signal.connect(self.result_table_init)
        self.search_controller.update_signal.connect(self.update_result_table)
        self.search_controller.model.id = self.ui.searchLineEdit.text()
        self.search_controller.start()
        self.ui.infoLabel.setText("正在加载...")

    @Slot(dict)
    def result_table_init(self, result):
        cnt = result["track_count"]
        self.ui.resultTableWidget.setRowCount(cnt)
        for i in range(cnt):
            self.ui.resultTableWidget.hideRow(i)
        self.ui.infoLabel.setText(f"正在加载歌单\"{result["title"]}\"...")

    @Slot(Music)
    def update_result_table(self, result):
        # 新建一个列
        new_frame = Ui_Frame()
        frame_widget = QWidget()
        new_frame.setupUi(frame_widget)
        new_frame.titleLabel.setText(result["title"])
        new_frame.artistLabel.setText(result["artist"])
        img = QImage.fromData(result["data"] if result["data"] != b"" else DEFAULT_COVER)
        new_frame.coverLabel.setImage(img)
        new_frame.coverLabel.setBorderRadius(8, 8, 8, 8)
        check_box = qfluentwidgets.CheckBox()
        # check_box.stateChanged.connect(self.table_clicked)
        self.ui.resultTableWidget.setCellWidget(result["index"], 2, check_box)
        self.ui.resultTableWidget.showRow(result["index"])
        self.ui.resultTableWidget.setRowHeight(result["index"], 64)
        self.ui.resultTableWidget.setCellWidget(result["index"], 1, frame_widget)
        self.ui.resultTableWidget.setItem(result["index"], 0, QTableWidgetItem(f"{result["index"]}"))
        self.ui.infoLabel.setText(f"正在加载歌单\"{result["from"]}\"...已加载{result["index"]}/{result["row"]}")
        self.update()

