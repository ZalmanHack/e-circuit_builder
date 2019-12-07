import sys

from interfaces import activationWindowUI
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget

class MiniWidget_signals(QObject):
    dial_changed = pyqtSignal(int)

class ActivationWindow(QWidget, activationWindowUI.Ui_Form):
    send_key = pyqtSignal(str)
    def __init__(self, parent=None, time_left: int = 0, key_len: int = 0):
        super().__init__(parent)
        self.setupUi(self)
        self.key_len = key_len
        self.time_left = time_left
        self.initUI()

    def initUI(self):
        self.set_label_time(self.time_left)
        self.lineEditKey.setVisible(False)
        self.lineEditKey.setMaxLength(self.key_len)
        self.pushFree.setEnabled(False)
        if self.time_left > 0:
            self.pushFree.setEnabled(True)

    @pyqtSlot(int)
    def set_label_time(self, time_left: int = 0):
        self.time_left = time_left
        self.label_time.setText("{0} мин. {1} сек.".format(int(self.time_left/60), self.time_left % 60))

    @pyqtSlot()
    def on_pushExit_clicked(self):
        sys.exit(0)

    @pyqtSlot()
    def on_pushKey_clicked(self):
        self.lineEditKey.clear()
        self.lineEditKey.setVisible(True)

    @pyqtSlot(str)
    def on_lineEditKey_textChanged(self, text):
        if len(text) == self.lineEditKey.maxLength():
            print("on_lineEditKey_textChanged")
            self.send_key.emit(text)