# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'working_keypad.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(251, 180, 51, 34))
        self.button_1.setObjectName("button_1")
        
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(251, 240, 51, 34))
        self.button_4.setObjectName("button_4")
        
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(340, 180, 51, 34))
        self.button_2.setObjectName("button_2")
        
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(340, 240, 51, 34))
        self.button_5.setObjectName("button_5")
        
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(251, 300, 51, 34))
        self.button_7.setObjectName("button_7")
        
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(340, 300, 51, 34))
        self.button_8.setObjectName("button_8")
        
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(430, 180, 51, 34))
        self.button_3.setObjectName("button_3")
        
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(430, 240, 51, 34))
        self.button_6.setObjectName("button_6")
        
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(430, 300, 51, 34))
        self.button_9.setObjectName("button_9")
        
        self.button_dot = QtWidgets.QPushButton(self.centralwidget)
        self.button_dot.setGeometry(QtCore.QRect(250, 360, 51, 34))
        self.button_dot.setObjectName("button_dot")
        
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(340, 360, 51, 34))
        self.button_0.setObjectName("button_0")
        
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(430, 360, 51, 34))
        self.delete_button.setObjectName("delete_button")
        
        self.menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.menu_button.setGeometry(QtCore.QRect(70, 190, 112, 34))
        self.menu_button.setObjectName("menu_button")
        
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setGeometry(QtCore.QRect(70, 250, 112, 34))
        self.quit_button.setObjectName("quit_button")
        
        self.reboot_button = QtWidgets.QPushButton(self.centralwidget)
        self.reboot_button.setGeometry(QtCore.QRect(70, 310, 112, 34))
        self.reboot_button.setObjectName("reboot_button")
        
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(550, 310, 112, 34))
        self.stop_button.setObjectName("stop_button")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(550, 190, 112, 34))
        self.start_button.setObjectName("start_button")
        
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(550, 250, 112, 34))
        self.pause_button.setObjectName("pause_button")
        
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(570, 110, 71, 51))
        self.ok_button.setObjectName("ok_button")
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(50,50,231,51))
        self.label1.setObjectName("label1")
        

        self.value_box = QtWidgets.QTextEdit(self.centralwidget)
        self.value_box.setGeometry(QtCore.QRect(250, 110, 231, 51))
        self.value_box.setObjectName("value_box")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
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
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.delete_button.setText(_translate("MainWindow", "DEL"))
        self.menu_button.setText(_translate("MainWindow", "Menu"))
        self.quit_button.setText(_translate("MainWindow", "Quit"))
        self.reboot_button.setText(_translate("MainWindow", "Reboot"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.pause_button.setText(_translate("MainWindow", "Pause"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.label1.setText(_translate("MainWindow", "TESTING"))

