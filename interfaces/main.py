import sys
import mainWindow
import miniWidget_logic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.Qt import *

class MainWindow(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.test = 0

    def initUI(self):
        #self.thread = QThread()
        self.miniWin = miniWidget_logic.MiniWidget_logic()
        self.miniWin.dial.valueChanged.connect(self.dial_valurChanged)
        #self.miniWin.moveToThread(self.thread)
        #self.thread.start()
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


    def dial_valurChanged(self, value: int):
        self.label.setText(str(value))

    def closeEvent(self, event):
        self.miniWin.close()
        return super(MainWindow, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
