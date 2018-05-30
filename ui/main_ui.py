# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_output.setGeometry(QtCore.QRect(20, 10, 971, 311))
        self.text_output.setObjectName("text_output")
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(20, 340, 31, 16))
        self.label_port.setObjectName("label_port")
        self.label_baud = QtWidgets.QLabel(self.centralwidget)
        self.label_baud.setGeometry(QtCore.QRect(20, 370, 41, 16))
        self.label_baud.setObjectName("label_baud")
        self.combobox_serial_port = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_serial_port.setGeometry(QtCore.QRect(60, 340, 181, 25))
        self.combobox_serial_port.setObjectName("combobox_serial_port")
        self.combobox_seial_baudrate = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_seial_baudrate.setGeometry(QtCore.QRect(60, 370, 101, 25))
        self.combobox_seial_baudrate.setObjectName("combobox_seial_baudrate")
        self.button_open_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_open_close.setGeometry(QtCore.QRect(182, 370, 101, 26))
        self.button_open_close.setObjectName("button_open_close")
        self.button_fresh = QtWidgets.QPushButton(self.centralwidget)
        self.button_fresh.setGeometry(QtCore.QRect(250, 340, 31, 26))
        self.button_fresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/fresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_fresh.setIcon(icon)
        self.button_fresh.setObjectName("button_fresh")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 26))
        self.menubar.setObjectName("menubar")
        self.menuCom = QtWidgets.QMenu(self.menubar)
        self.menuCom.setObjectName("menuCom")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_fresh = QtWidgets.QAction(MainWindow)
        self.action_fresh.setShortcut("")
        self.action_fresh.setObjectName("action_fresh")
        self.menuCom.addAction(self.action_fresh)
        self.menubar.addAction(self.menuCom.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_port.setText(_translate("MainWindow", "Port"))
        self.label_baud.setText(_translate("MainWindow", "Baud"))
        self.button_open_close.setText(_translate("MainWindow", "Open"))
        self.menuCom.setTitle(_translate("MainWindow", "Com"))
        self.action_fresh.setText(_translate("MainWindow", "Fresh"))

import resource_rc
