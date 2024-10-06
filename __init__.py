from PySide6.QtWidgets import QApplication
import sys
from controller import Application

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_controller = Application()
    app_controller.mainwindow_view.show()
    app.exec()
