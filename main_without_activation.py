import sys
from PyQt5.Qt import QApplication, QMessageBox

from interfaces.mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
