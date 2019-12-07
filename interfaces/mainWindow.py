import sys
import time
from functions import ecircuit
from interfaces import mainWindowUI
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.Qt import *

class MainWindow(QMainWindow, mainWindowUI.Ui_MainWindow):
    closed = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # инициализация таблицы ----------------------------------------------------------------------------------------
        self.model = QStandardItemModel()
        self.model.setColumnCount(3)
        self.model.setRowCount(2)
        self.model.setHorizontalHeaderLabels(["1","2","3"])
        self.model.setItem(0,0,QStandardItem("START"))
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        # подключение сигналов -----------------------------------------------------------------------------------------
        self.tableView.clicked.connect(self.tableView_clicked)
        self.pushClear.clicked.connect(self.pushClear_clicked)
        self.pushBuilding.clicked.connect(self.pushBuilding_clicked)

    def tableView_clicked(self, index: QModelIndex):
        if index.row() == self.model.rowCount()-1:
            self.model.appendRow([QStandardItem(), QStandardItem(), QStandardItem()])

    def pushClear_clicked(self):
        self.initUI()

    def pushBuilding_clicked(self):
        items = []
        for row in range(0,self.model.rowCount()):
            rowItems = []
            for column in range(0, self.model.columnCount()):
                if self.model.index(row, column).data() is not None:
                    rowItems.append(self.model.index(row, column).data())
            if len(rowItems) == self.model.columnCount():
                print(rowItems)
                items.append(rowItems)

    def dial_valurChanged(self, value: int):
        self.label.setText(str(value))

    def closeEvent(self, event):
        self.closed.emit()
        return super(MainWindow, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
