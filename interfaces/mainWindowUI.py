# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 721)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.panelECircuit = QtWidgets.QWidget(self.mainWidget)
        self.panelECircuit.setStyleSheet("QWidget {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213)\n"
"}")
        self.panelECircuit.setObjectName("panelECircuit")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.panelECircuit)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.panelECircuit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setStyleSheet("QLabel {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_4.addWidget(self.panelECircuit)
        self.panelBranches = QtWidgets.QWidget(self.mainWidget)
        self.panelBranches.setStyleSheet("QWidget {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213)\n"
"}")
        self.panelBranches.setObjectName("panelBranches")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.panelBranches)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.panelBranches)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setStyleSheet("QLabel {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.panelBranches)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    border-width: 0;\n"
"    selection-background-color: rgb(220, 220, 220);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addWidget(self.panelBranches)
        self.horizontalLayout.addWidget(self.mainWidget)
        self.panelTable = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panelTable.sizePolicy().hasHeightForWidth())
        self.panelTable.setSizePolicy(sizePolicy)
        self.panelTable.setMinimumSize(QtCore.QSize(300, 0))
        self.panelTable.setMaximumSize(QtCore.QSize(300, 16777215))
        self.panelTable.setStyleSheet("QWidget {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213);\n"
"}")
        self.panelTable.setObjectName("panelTable")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.panelTable)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.panelTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setStyleSheet("QLabel {\n"
"background-color: rgb(240, 240, 240);\n"
"border-width: 1px;\n"
"border-right-width: 0;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.tableView = QtWidgets.QTableView(self.panelTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView.setStyleSheet("QTableView {\n"
"    border-left-width: 1px;\n"
"    selection-background-color: rgb(240, 240, 240);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}")
        self.tableView.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableView.setLineWidth(0)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout.addWidget(self.panelTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFunctions = QtWidgets.QMenu(self.menubar)
        self.menuFunctions.setObjectName("menuFunctions")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        MainWindow.setMenuBar(self.menubar)
        self.pushExport = QtWidgets.QAction(MainWindow)
        self.pushExport.setObjectName("pushExport")
        self.pushMinimization = QtWidgets.QAction(MainWindow)
        self.pushMinimization.setObjectName("pushMinimization")
        self.pushStructuring = QtWidgets.QAction(MainWindow)
        self.pushStructuring.setObjectName("pushStructuring")
        self.pushDestructuring = QtWidgets.QAction(MainWindow)
        self.pushDestructuring.setObjectName("pushDestructuring")
        self.pushClear = QtWidgets.QAction(MainWindow)
        self.pushClear.setObjectName("pushClear")
        self.pushAboutProgram = QtWidgets.QAction(MainWindow)
        self.pushAboutProgram.setObjectName("pushAboutProgram")
        self.showECircuit = QtWidgets.QAction(MainWindow)
        self.showECircuit.setObjectName("showECircuit")
        self.showBranches = QtWidgets.QAction(MainWindow)
        self.showBranches.setObjectName("showBranches")
        self.showTable = QtWidgets.QAction(MainWindow)
        self.showTable.setObjectName("showTable")
        self.pushSave = QtWidgets.QAction(MainWindow)
        self.pushSave.setObjectName("pushSave")
        self.pushOpen = QtWidgets.QAction(MainWindow)
        self.pushOpen.setObjectName("pushOpen")
        self.menuFile.addAction(self.pushOpen)
        self.menuFile.addAction(self.pushSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.pushExport)
        self.menuFunctions.addAction(self.pushMinimization)
        self.menuFunctions.addAction(self.pushStructuring)
        self.menuFunctions.addSeparator()
        self.menuFunctions.addAction(self.pushClear)
        self.menuInfo.addAction(self.pushAboutProgram)
        self.menuWindows.addAction(self.showECircuit)
        self.menuWindows.addAction(self.showBranches)
        self.menuWindows.addAction(self.showTable)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFunctions.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Е-Схема"))
        self.label.setText(_translate("MainWindow", "Ветви"))
        self.label_2.setText(_translate("MainWindow", "Таблица смежности"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menuFunctions.setTitle(_translate("MainWindow", "Операции"))
        self.menuInfo.setTitle(_translate("MainWindow", "Справка"))
        self.menuWindows.setTitle(_translate("MainWindow", "Окно"))
        self.pushExport.setText(_translate("MainWindow", "Экспорт"))
        self.pushExport.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.pushMinimization.setText(_translate("MainWindow", "Минимизация"))
        self.pushMinimization.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.pushStructuring.setText(_translate("MainWindow", "Структурирование"))
        self.pushStructuring.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushDestructuring.setText(_translate("MainWindow", "Деструктурирование"))
        self.pushClear.setText(_translate("MainWindow", "Очистка"))
        self.pushClear.setShortcut(_translate("MainWindow", "Shift+C"))
        self.pushAboutProgram.setText(_translate("MainWindow", "О приложении"))
        self.showECircuit.setText(_translate("MainWindow", "Схема"))
        self.showECircuit.setToolTip(_translate("MainWindow", "Вкл/Вык отображения схемы"))
        self.showECircuit.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.showBranches.setText(_translate("MainWindow", "Ветвления"))
        self.showBranches.setToolTip(_translate("MainWindow", "Вкл/Вык отображения ветвлений"))
        self.showBranches.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.showTable.setText(_translate("MainWindow", "Таблица смежности"))
        self.showTable.setToolTip(_translate("MainWindow", "Вкл/Вык отображения таблицы смежности"))
        self.showTable.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.pushSave.setText(_translate("MainWindow", "Сохранить"))
        self.pushOpen.setText(_translate("MainWindow", "Открыть"))
