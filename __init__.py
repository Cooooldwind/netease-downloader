from PySide6.QtWidgets import QApplication
import sys
from view.main_window import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
