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
        MainWindow.resize(910, 571)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
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
        self.widget = QtWidgets.QWidget(self.panelECircuit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 20))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setStyleSheet("QLabel {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.closeECircuit = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeECircuit.sizePolicy().hasHeightForWidth())
        self.closeECircuit.setSizePolicy(sizePolicy)
        self.closeECircuit.setMinimumSize(QtCore.QSize(20, 0))
        self.closeECircuit.setMaximumSize(QtCore.QSize(20, 16777215))
        self.closeECircuit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeECircuit.setWhatsThis("")
        self.closeECircuit.setAccessibleName("")
        self.closeECircuit.setAccessibleDescription("")
        self.closeECircuit.setStyleSheet("QPushButton {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"color: rgb(93, 93, 93)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(220, 220, 220);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(240, 240, 240);\n"
"}\n"
"")
        self.closeECircuit.setObjectName("closeECircuit")
        self.horizontalLayout_2.addWidget(self.closeECircuit)
        self.verticalLayout_2.addWidget(self.widget)
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
        self.widget1 = QtWidgets.QWidget(self.panelBranches)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMinimumSize(QtCore.QSize(0, 20))
        self.widget1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget1)
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
        self.horizontalLayout_3.addWidget(self.label)
        self.closeBranches = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBranches.sizePolicy().hasHeightForWidth())
        self.closeBranches.setSizePolicy(sizePolicy)
        self.closeBranches.setMinimumSize(QtCore.QSize(20, 0))
        self.closeBranches.setMaximumSize(QtCore.QSize(20, 16777215))
        self.closeBranches.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBranches.setStyleSheet("QPushButton {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"color: rgb(93, 93, 93)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(220, 220, 220);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(240, 240, 240);\n"
"}")
        self.closeBranches.setObjectName("closeBranches")
        self.horizontalLayout_3.addWidget(self.closeBranches)
        self.verticalLayout.addWidget(self.widget1)
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
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        self.horizontalLayout_5.addWidget(self.mainWidget)
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
        self.widget2 = QtWidgets.QWidget(self.panelTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget2.sizePolicy().hasHeightForWidth())
        self.widget2.setSizePolicy(sizePolicy)
        self.widget2.setMinimumSize(QtCore.QSize(0, 20))
        self.widget2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget2)
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
        self.horizontalLayout_4.addWidget(self.label_2)
        self.closeTable = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeTable.sizePolicy().hasHeightForWidth())
        self.closeTable.setSizePolicy(sizePolicy)
        self.closeTable.setMinimumSize(QtCore.QSize(20, 0))
        self.closeTable.setMaximumSize(QtCore.QSize(20, 16777215))
        self.closeTable.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeTable.setStyleSheet("QPushButton {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"color: rgb(93, 93, 93)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(220, 220, 220);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(93, 93, 93);\n"
"color: rgb(240, 240, 240);\n"
"}")
        self.closeTable.setObjectName("closeTable")
        self.horizontalLayout_4.addWidget(self.closeTable)
        self.verticalLayout_3.addWidget(self.widget2)
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
        self.horizontalLayout_5.addWidget(self.panelTable)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelBranches = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBranches.sizePolicy().hasHeightForWidth())
        self.labelBranches.setSizePolicy(sizePolicy)
        self.labelBranches.setMinimumSize(QtCore.QSize(0, 20))
        self.labelBranches.setStyleSheet("QLabel {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213);\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1px;\n"
"border-right-width: 1px;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.labelBranches.setText("")
        self.labelBranches.setObjectName("labelBranches")
        self.horizontalLayout.addWidget(self.labelBranches)
        self.labelElements = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelElements.sizePolicy().hasHeightForWidth())
        self.labelElements.setSizePolicy(sizePolicy)
        self.labelElements.setMinimumSize(QtCore.QSize(0, 20))
        self.labelElements.setStyleSheet("QLabel {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213);\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1px;\n"
"border-right-width: 1px;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.labelElements.setText("")
        self.labelElements.setObjectName("labelElements")
        self.horizontalLayout.addWidget(self.labelElements)
        self.labelKnots = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelKnots.sizePolicy().hasHeightForWidth())
        self.labelKnots.setSizePolicy(sizePolicy)
        self.labelKnots.setMinimumSize(QtCore.QSize(0, 20))
        self.labelKnots.setStyleSheet("QLabel {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213);\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1px;\n"
"border-right-width: 1px;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.labelKnots.setText("")
        self.labelKnots.setObjectName("labelKnots")
        self.horizontalLayout.addWidget(self.labelKnots)
        self.labelEmty = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEmty.sizePolicy().hasHeightForWidth())
        self.labelEmty.setSizePolicy(sizePolicy)
        self.labelEmty.setMinimumSize(QtCore.QSize(0, 20))
        self.labelEmty.setStyleSheet("QLabel {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213);\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.labelEmty.setText("")
        self.labelEmty.setObjectName("labelEmty")
        self.horizontalLayout.addWidget(self.labelEmty)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
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
        self.closeECircuit.setText(_translate("MainWindow", "✖"))
        self.label.setText(_translate("MainWindow", "Ветви"))
        self.closeBranches.setText(_translate("MainWindow", "✖"))
        self.label_2.setText(_translate("MainWindow", "Таблица смежности"))
        self.closeTable.setText(_translate("MainWindow", "✖"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menuFunctions.setTitle(_translate("MainWindow", "Операции"))
        self.menuInfo.setTitle(_translate("MainWindow", "Справка"))
        self.menuWindows.setTitle(_translate("MainWindow", "Окно"))
        self.pushExport.setText(_translate("MainWindow", "Экспорт"))
        self.pushExport.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.pushMinimization.setText(_translate("MainWindow", "Минимизация"))
        self.pushMinimization.setShortcut(_translate("MainWindow", "Shift+M"))
        self.pushStructuring.setText(_translate("MainWindow", "Структурирование"))
        self.pushStructuring.setShortcut(_translate("MainWindow", "Shift+S"))
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
        self.pushSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushOpen.setText(_translate("MainWindow", "Открыть"))
        self.pushOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
