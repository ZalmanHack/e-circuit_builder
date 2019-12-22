import sys
import pickle
from functions.ecircuit import ECircuit
from interfaces import mainWindowUI
from interfaces.myGraphicsView import MyGraphicView
from PyQt5.Qt import *

class MainWindow(QMainWindow, mainWindowUI.Ui_MainWindow):
    class SignalsForECircuit(QObject):
        setTable = pyqtSignal(list)
        getMatrix = pyqtSignal()
        startBuild = pyqtSignal()
        startMinimize = pyqtSignal()
        startStruct = pyqtSignal()

    closed = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.initECircuit()

    def initUI(self):
        self.setWindowIcon(QIcon('./icons/icon.ico'))
        self.window().setWindowTitle("Построитель Е-Схем")
        # инициализация таблицы ----------------------------------------------------------------------------------------
        self.initModel()
        # инициализация своей графической сцены ------------------------------------------------------------------------
        self.graphicView = MyGraphicView(self)
        self.gridLayout.addWidget(self.graphicView)
        # инициализация текстового отображения ветвей-------------------------------------------------------------------
        font = QFont()
        font.setPixelSize(14)
        font.setBold(False)
        font.setFamily("Arial")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        # инициализация кнопок отображения окон ------------------------------------------------------------------------
        self.showECircuit.setCheckable(True)
        self.showBranches.setCheckable(True)
        self.showTable.setCheckable(True)
        self.showECircuit.setChecked(True)
        self.showBranches.setChecked(True)
        self.showTable.setChecked(True)
        # инициализируем нижний блок -----------------------------------------------------------------------------------
        self.setBottomInfo()
        # отключения элементов -------------------------- ! ! ! ! ! ! --------------------------------------------------
        # self.pushMinimization.deleteLater()
        # self.pushStructuring.deleteLater()
        # self.pushDestructuring.deleteLater()
        self.menuInfo.deleteLater()

    def initModel(self):
        self.model = QStandardItemModel()
        self.model.setColumnCount(3)
        self.model.setRowCount(1)
        self.model.setItem(0,0,QStandardItem("START"))
        self.model.dataChanged.connect(self.on_model_dataChanged)
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
        self.ec_signals.startStruct.connect(self.e_circuit.structuring)
        self.e_circuit.built.connect(self.built)  # сообщение от построителя с матрицей и дллиной текста
        self.e_circuit.error.connect(self.msg_error)
        self.e_circuit.moveToThread(self.e_circuit_thread)
        self.e_circuit_thread.start()

    @pyqtSlot(QModelIndex)
    def on_model_dataChanged(self, index: QModelIndex):
        for column in range(0, self.model.columnCount()):
            if self.model.index(index.row(),column).data() is None or self.model.index(index.row(),column).data() == '':
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

    @pyqtSlot()
    def on_pushClear_triggered(self):
        self.initModel()
        self.items.clear()
        self.plainTextEdit.clear()
        self.graphicView.scene.clear()
        self.graphicView.scene.setSceneRect(0, 0, 50, 50)
        self.setBottomInfo()

    @pyqtSlot()
    def on_pushMinimization_triggered(self):
        self.ec_signals.setTable.emit(self.items)
        self.ec_signals.startMinimize.emit()

    @pyqtSlot()
    def on_pushStructuring_triggered(self):
        self.ec_signals.setTable.emit(self.items)
        self.ec_signals.startStruct.emit()

    @pyqtSlot()
    def on_pushExport_triggered(self):
        file_name = QFileDialog.getSaveFileName(self, "Сохранить файл как", "Схема", "PNG(*.png)")
        if file_name[0] != '':
            image = QImage(self.graphicView.scene.width()*2, self.graphicView.scene.height()*2, QImage.Format_ARGB32_Premultiplied)
            image.fill(QColor(Qt.white))
            painter = QPainter(image)
            painter.setRenderHint(QPainter.Antialiasing)
            self.graphicView.scene.render(painter)
            painter.end()
            image.save(file_name[0])

    @pyqtSlot()
    def on_pushSave_triggered(self):
        file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", "Схема", "ECB(*.ecb)")
        if file_name[0] != '':
            with open(file_name[0], 'wb') as file:
                pickle.dump(self.items, file)

    @pyqtSlot()
    def on_pushOpen_triggered(self):
        file_name = QFileDialog.getOpenFileName(self, "Открыть файл", "Схема", "ECB(*.ecb)")
        if file_name[0] != '':
            with open(file_name[0], 'rb') as file:
                info = pickle.load(file)
                if type(info) == list and len(info) > 0:
                    self.on_pushClear_triggered()
                    self.model.setRowCount(0)
                    for row in info:
                        self.model.appendRow([QStandardItem(row[0]), QStandardItem(row[1]), QStandardItem(row[2])])
                        self.items.append([row[0], row[1], row[2]])
                    self.ec_signals.setTable.emit(self.items)
                    self.ec_signals.startBuild.emit()

    @pyqtSlot()
    def on_showECircuit_triggered(self):
        self.panelECircuit.setVisible(self.showECircuit.isChecked())

    @pyqtSlot()
    def on_showBranches_triggered(self):
        self.panelBranches.setVisible(self.showBranches.isChecked())

    @pyqtSlot()
    def on_showTable_triggered(self):
        self.panelTable.setVisible(self.showTable.isChecked())

    @pyqtSlot()
    def on_closeTable_clicked(self):
        self.showTable.setChecked(False)
        self.on_showTable_triggered()

    @pyqtSlot()
    def on_closeECircuit_clicked(self):
        self.showECircuit.setChecked(False)
        self.on_showECircuit_triggered()

    @pyqtSlot()
    def on_closeBranches_clicked(self):
        self.showBranches.setChecked(False)
        self.on_showBranches_triggered()

    @pyqtSlot(QCloseEvent)
    def closeEvent(self, event):
        self.closed.emit()
        return super(MainWindow, self).closeEvent(event)

    @pyqtSlot(str)
    def msg_error(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Сообщение")
        msg.exec_()

    @pyqtSlot(list, list, list, int, int)
    def built(self, branches: list, matrix: list, items: list, textLen: int, quantityKnots: int):
        if items:
            self.items = items
            self.updateTableView(items)
        # считаем кол-во элементов
        elements = []
        for row in self.items:
            if row[0] != "START" and row[0] not in elements:
                elements.append(row[0])
        # отображаем данные
        self.updateGraphisView(matrix, textLen)
        self.updateBranchesText(branches)
        self.setBottomInfo(len(branches), len(elements), quantityKnots)

    def setBottomInfo(self, branches: int = 0, quantityElements: int = 0, quantityKnots: int = 0):
        self.labelBranches.setText("Ветви: {0}".format(branches))
        self.labelElements.setText("Элементы: {0}".format(quantityElements))
        self.labelKnots.setText("Узлы: {0}".format(quantityKnots))
        self.labelEmty.setText("Данные взяты из таблицы смежности")

    @pyqtSlot(list)
    def updateBranchesText(self, branches: list):
        self.plainTextEdit.clear()
        number = 1
        for branch in branches:
            self.plainTextEdit.appendPlainText("{0})  {1}".format(number, "---".join(branch)))
            number += 1

    @pyqtSlot(list)
    def updateTableView(self, items: list):
        if len(items) > 0:
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
        if len(matrix) > 0:
            self.graphicView.setMatrix(matrix)
            self.graphicView.setTextSetting(textLen, 25)
            self.graphicView.draw()
        else:
            self.graphicView.scene.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
