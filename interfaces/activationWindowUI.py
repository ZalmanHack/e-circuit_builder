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
        Form.resize(500, 146)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 146))
        Form.setMaximumSize(QtCore.QSize(500, 146))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.widgetTime = QtWidgets.QWidget(Form)
        self.widgetTime.setStyleSheet("QWidget {\n"
"font: 25 16pt \"Segoe UI\";\n"
"}")
        self.widgetTime.setObjectName("widgetTime")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetTime)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widgetTime)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_time = QtWidgets.QLabel(self.widgetTime)
        self.label_time.setStyleSheet("")
        self.label_time.setObjectName("label_time")
        self.horizontalLayout.addWidget(self.label_time)
        self.verticalLayout_2.addWidget(self.widgetTime)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.widgetKey = QtWidgets.QWidget(Form)
        self.widgetKey.setStyleSheet("QWidget {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213)\n"
"}")
        self.widgetKey.setObjectName("widgetKey")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetKey)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widgetKey)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setStyleSheet("QLabel {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-left-width: 1;\n"
"border-right-width: 1;\n"
"color: rgb(93, 93, 93);\n"
"padding-left: 10px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEditKey = QtWidgets.QLineEdit(self.widgetKey)
        self.lineEditKey.setStyleSheet("QLineEdit {\n"
"    border-top-width: 1;\n"
"    border-bottom-width: 1;\n"
"    border-left-width: 1;\n"
"    border-right-width: 1;\n"
"    font: 25 16pt \"Segoe UI\";\n"
"}")
        self.lineEditKey.setInputMask("")
        self.lineEditKey.setText("")
        self.lineEditKey.setMaxLength(32767)
        self.lineEditKey.setFrame(True)
        self.lineEditKey.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditKey.setObjectName("lineEditKey")
        self.verticalLayout.addWidget(self.lineEditKey)
        self.verticalLayout_2.addWidget(self.widgetKey)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(0, 20))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget.setStyleSheet("QWidget {\n"
"border-style: solid;\n"
"border-color:  rgb(213, 213, 213)\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushFree = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushFree.sizePolicy().hasHeightForWidth())
        self.pushFree.setSizePolicy(sizePolicy)
        self.pushFree.setStyleSheet("QPushButton {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"border-left-width: 1;\n"
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
        self.pushFree.setObjectName("pushFree")
        self.horizontalLayout_2.addWidget(self.pushFree)
        self.pushKey = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushKey.sizePolicy().hasHeightForWidth())
        self.pushKey.setSizePolicy(sizePolicy)
        self.pushKey.setStyleSheet("QPushButton {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"border-left-width: 1;\n"
"border-right-width: 1;\n"
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
        self.pushKey.setObjectName("pushKey")
        self.horizontalLayout_2.addWidget(self.pushKey)
        self.pushExit = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushExit.sizePolicy().hasHeightForWidth())
        self.pushExit.setSizePolicy(sizePolicy)
        self.pushExit.setStyleSheet("QPushButton {\n"
"background-color: rgb(240, 240, 240);\n"
"border-top-width: 1;\n"
"border-bottom-width: 1;\n"
"border-right-width: 1;\n"
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
        self.pushExit.setObjectName("pushExit")
        self.horizontalLayout_2.addWidget(self.pushExit)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Пробный период"))
        self.label_time.setText(_translate("Form", "0 мин. 0 сек."))
        self.label_3.setText(_translate("Form", "Поля для ввода ключа активации"))
        self.lineEditKey.setPlaceholderText(_translate("Form", "Ключ"))
        self.pushFree.setText(_translate("Form", "Начать пробный период"))
        self.pushKey.setText(_translate("Form", "Ввести ключ активации"))
        self.pushExit.setText(_translate("Form", "Выход из программы"))
