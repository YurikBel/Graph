# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1154, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Grahps_list = QtWidgets.QListWidget(self.centralwidget)
        self.Grahps_list.setGeometry(QtCore.QRect(80, 70, 251, 531))
        self.Grahps_list.setObjectName("Grahps_list")
        self.table_values = QtWidgets.QTableWidget(self.centralwidget)
        self.table_values.setGeometry(QtCore.QRect(400, 70, 361, 531))
        self.table_values.setObjectName("table_values")
        self.table_values.setColumnCount(0)
        self.table_values.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 131, 20))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_graph_name = QtWidgets.QLabel(self.centralwidget)
        self.label_graph_name.setGeometry(QtCore.QRect(510, 20, 151, 21))
        self.label_graph_name.setText("")
        self.label_graph_name.setObjectName("label_graph_name")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(480, 40, 111, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(80, 60, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 310, 121, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_delete_graph = QtWidgets.QAction(MainWindow)
        self.action_delete_graph.setObjectName("action_delete_graph")
        self.action_create_graph = QtWidgets.QAction(MainWindow)
        self.action_create_graph.setObjectName("action_create_graph")
        self.action_edit = QtWidgets.QAction(MainWindow)
        self.action_edit.setObjectName("action_edit")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addSeparator()
        self.menu.addSeparator()
        self.menu.addAction(self.action_delete_graph)
        self.menu.addAction(self.action_create_graph)
        self.menu.addAction(self.action_edit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Мои графики:"))
        self.pushButton.setText(_translate("MainWindow", "Построить график"))
        self.menu.setTitle(_translate("MainWindow", "График"))
        self.action_delete_graph.setText(_translate("MainWindow", "Удалить"))
        self.action_create_graph.setText(_translate("MainWindow", "Создать"))
        self.action_edit.setText(_translate("MainWindow", "Редактировать"))
        self.action_2.setText(_translate("MainWindow", "Построить "))