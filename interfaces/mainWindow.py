import sys
import time
from functions.ecircuit import ECircuit
from interfaces import mainWindowUI
from interfaces.myGraphicsView import MyGraphicView
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.Qt import *

class MainWindow(QMainWindow, mainWindowUI.Ui_MainWindow):
    class SignalsForECircuit(QObject):
        setTable = pyqtSignal(list)
        getMatrix = pyqtSignal()
        startBuild = pyqtSignal()
        startMinimize = pyqtSignal()

    closed = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.initECircuit()

    def initUI(self):
        # инициализация таблицы ----------------------------------------------------------------------------------------
        self.initModel()
        # инициализация своей графической сцены ------------------------------------------------------------------------
        self.graphicView = MyGraphicView(self)
        self.gridLayout.addWidget(self.graphicView)
        # подключение сигналов -----------------------------------------------------------------------------------------
        self.pushClear.clicked.connect(self.pushClear_clicked)
        self.pushBuilding.clicked.connect(self.pushBuilding_clicked)
        self.pushMinimization.clicked.connect(self.pushMinimization_clicked)

    def initModel(self):
        self.model = QStandardItemModel()
        self.model.setColumnCount(3)
        self.model.setRowCount(1)
        self.model.setHorizontalHeaderLabels(["1","2","3"])
        self.model.setItem(0,0,QStandardItem("START"))
        self.model.dataChanged.connect(self.model_dataChanged)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

    def initECircuit(self):
        self.items = []
        self.ec_signals = self.SignalsForECircuit()
        self.e_circuit_thread = QThread(self)
        self.e_circuit = ECircuit()
        self.ec_signals.setTable.connect(self.e_circuit.setTable)
        self.ec_signals.startBuild.connect(self.e_circuit.build)
        self.ec_signals.startMinimize.connect(self.e_circuit.minimize)
        self.e_circuit.built.connect(self.updateGraphisView)  # сообщение от построителя с матрицей и дллиной текста
        self.e_circuit.minimized.connect(self.minimized)
        self.e_circuit.moveToThread(self.e_circuit_thread)
        self.e_circuit_thread.start()

    def model_dataChanged(self, index: QModelIndex):
        print(index.row(), index.column())
        for column in range(0, self.model.columnCount()):
            if self.model.index(index.row(), column).data() is None:
                return
        if index.row() == self.model.rowCount()-1:
            self.model.appendRow([QStandardItem(), QStandardItem(), QStandardItem()])
        if index.row() not in range(0, len(self.items)):
            temp_row = []
            for column in range(0, self.model.columnCount()):
                temp_row.append(self.model.index(index.row(), column).data())
            self.items.append(temp_row)
            self.ec_signals.setTable.emit(self.items)
            self.ec_signals.startBuild.emit()
            return
        if self.items[index.row()][index.column()] != self.model.index(index.row(), index.column()).data():
            self.items[index.row()][index.column()] = self.model.index(index.row(), index.column()).data()
            self.ec_signals.setTable.emit(self.items)
            self.ec_signals.startBuild.emit()
            return

    def pushClear_clicked(self):
        self.initModel()
        self.items.clear()
        self.graphicView.scene.clear()

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
        if items:
            self.ec_signals.setTable.emit(items)
            self.ec_signals.startBuild.emit()

    def pushMinimization_clicked(self):
        self.ec_signals.setTable.emit(self.items)
        self.ec_signals.startMinimize.emit()

    def closeEvent(self, event):
        self.closed.emit()
        return super(MainWindow, self).closeEvent(event)

    @pyqtSlot(list, list, int)
    def minimized(self, matrix: list, items: list, textLen: int):
        self.updateGraphisView(matrix, textLen)
        self.updateTableView(items)

    def updateTableView(self, items: list):
        self.initModel()
        self.model.setRowCount(0)
        self.model.itemData(QModelIndex()).clear()
        self.items = items
        for row in range(0, len(self.items)):
            items_row = []
            for column in range(0, len(self.items[row])):
                items_row.append(QStandardItem(self.items[row][column]))
            self.model.appendRow(items_row)


    @pyqtSlot(list, int)
    def updateGraphisView(self, matrix: list, textLen: int):
        self.graphicView.setMatrix(matrix)
        self.graphicView.setTextSetting(textLen, 15)
        self.graphicView.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
