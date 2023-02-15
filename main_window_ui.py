# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 349)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 151, 41))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_1.setGeometry(QtCore.QRect(190, 230, 99, 16))
        self.doubleSpinBox_1.setDecimals(3)
        self.doubleSpinBox_1.setMaximum(2000000.0)
        self.doubleSpinBox_1.setProperty("value", 5.0)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(300, 230, 99, 16))
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setMaximum(2000000.0)
        self.doubleSpinBox_2.setProperty("value", 30.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(410, 230, 99, 16))
        self.doubleSpinBox_3.setDecimals(3)
        self.doubleSpinBox_3.setMaximum(2000000.0)
        self.doubleSpinBox_3.setProperty("value", 5.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 50, 451, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("figures/start_stop_signal.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(520, 230, 99, 16))
        self.doubleSpinBox_4.setDecimals(3)
        self.doubleSpinBox_4.setMaximum(2000000.0)
        self.doubleSpinBox_4.setProperty("value", 5.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 260, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 260, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 180, 121, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton.raise_()
        self.label.raise_()
        self.doubleSpinBox_1.raise_()
        self.doubleSpinBox_2.raise_()
        self.doubleSpinBox_3.raise_()
        self.doubleSpinBox_4.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enable/Disable\n"
"Remote Control"))
        self.doubleSpinBox_1.setSuffix(_translate("MainWindow", " ms"))
        self.doubleSpinBox_2.setSuffix(_translate("MainWindow", " ms"))
        self.doubleSpinBox_3.setSuffix(_translate("MainWindow", " ms"))
        self.doubleSpinBox_4.setSuffix(_translate("MainWindow", " ms"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.label_2.setText(_translate("MainWindow", "COM Port"))
