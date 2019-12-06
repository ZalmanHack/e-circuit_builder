import sys

import miniWidget

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget

class MiniWidget_signals(QObject):
    dial_changed = pyqtSignal(int)

class MiniWidget_logic(QWidget, miniWidget.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiniWidget_logic()
    window.show()
    sys.exit(app.exec())
