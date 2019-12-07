# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activationWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 167)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 167))
        Form.setMaximumSize(QtCore.QSize(500, 167))
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 16pt \"Segoe UI\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("font: 25 16pt \"Segoe UI\";")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_time = QtWidgets.QLabel(Form)
        self.label_time.setStyleSheet("font: 25 16pt \"Segoe UI\";")
        self.label_time.setObjectName("label_time")
        self.horizontalLayout.addWidget(self.label_time)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEditKey = QtWidgets.QLineEdit(Form)
        self.lineEditKey.setStyleSheet("font: 25 16pt \"Segoe UI\";")
        self.lineEditKey.setInputMask("")
        self.lineEditKey.setText("")
        self.lineEditKey.setMaxLength(32767)
        self.lineEditKey.setFrame(True)
        self.lineEditKey.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditKey.setObjectName("lineEditKey")
        self.verticalLayout.addWidget(self.lineEditKey)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushFree = QtWidgets.QPushButton(Form)
        self.pushFree.setObjectName("pushFree")
        self.horizontalLayout_2.addWidget(self.pushFree)
        self.pushKey = QtWidgets.QPushButton(Form)
        self.pushKey.setObjectName("pushKey")
        self.horizontalLayout_2.addWidget(self.pushKey)
        self.pushExit = QtWidgets.QPushButton(Form)
        self.pushExit.setObjectName("pushExit")
        self.horizontalLayout_2.addWidget(self.pushExit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Построитель Е-Схем"))
        self.label_2.setText(_translate("Form", "Пробный период"))
        self.label_time.setText(_translate("Form", "0 мин. 0 сек."))
        self.lineEditKey.setPlaceholderText(_translate("Form", "Введите ключ активации"))
        self.pushFree.setText(_translate("Form", "Начать пробный период"))
        self.pushKey.setText(_translate("Form", "Ввести ключ активации"))
        self.pushExit.setText(_translate("Form", "Выход из программы"))
