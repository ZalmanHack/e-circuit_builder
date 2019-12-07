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
        MainWindow.resize(918, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushBuilding = QtWidgets.QPushButton(self.centralwidget)
        self.pushBuilding.setObjectName("pushBuilding")
        self.horizontalLayout.addWidget(self.pushBuilding)
        self.pushMinimization = QtWidgets.QPushButton(self.centralwidget)
        self.pushMinimization.setMinimumSize(QtCore.QSize(100, 0))
        self.pushMinimization.setObjectName("pushMinimization")
        self.horizontalLayout.addWidget(self.pushMinimization)
        self.pushStructuring = QtWidgets.QPushButton(self.centralwidget)
        self.pushStructuring.setMinimumSize(QtCore.QSize(100, 0))
        self.pushStructuring.setObjectName("pushStructuring")
        self.horizontalLayout.addWidget(self.pushStructuring)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushExport = QtWidgets.QPushButton(self.centralwidget)
        self.pushExport.setObjectName("pushExport")
        self.horizontalLayout.addWidget(self.pushExport)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushClear.setObjectName("pushClear")
        self.horizontalLayout.addWidget(self.pushClear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.VLine)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphicsView.setLineWidth(0)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(200, 0))
        self.tableView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tableView.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableView.setLineWidth(0)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushBuilding.setText(_translate("MainWindow", "Построить"))
        self.pushMinimization.setText(_translate("MainWindow", "Минимизировать"))
        self.pushStructuring.setText(_translate("MainWindow", "Структурировать"))
        self.pushExport.setText(_translate("MainWindow", "Экспорт"))
        self.pushClear.setText(_translate("MainWindow", "Очистить"))
