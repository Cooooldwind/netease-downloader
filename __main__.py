import sys
from PySide6.QtWidgets import QApplication
from ui import MainPage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    app.exec()