# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(562, 608)
        self.pushButton_show_graph = QtWidgets.QPushButton(Form)
        self.pushButton_show_graph.setGeometry(QtCore.QRect(400, 100, 131, 28))
        self.pushButton_show_graph.setObjectName("pushButton_show_graph")
        self.lineEdit_teor = QtWidgets.QLineEdit(Form)
        self.lineEdit_teor.setGeometry(QtCore.QRect(50, 280, 161, 31))
        self.lineEdit_teor.setObjectName("lineEdit_teor")
        self.pushButton_differ = QtWidgets.QPushButton(Form)
        self.pushButton_differ.setGeometry(QtCore.QRect(330, 230, 181, 28))
        self.pushButton_differ.setObjectName("pushButton_differ")
        self.pushButton_show = QtWidgets.QPushButton(Form)
        self.pushButton_show.setGeometry(QtCore.QRect(330, 190, 151, 28))
        self.pushButton_show.setObjectName("pushButton_show")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(40, 70, 111, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox_points = QtWidgets.QCheckBox(Form)
        self.checkBox_points.setGeometry(QtCore.QRect(50, 130, 121, 20))
        self.checkBox_points.setObjectName("checkBox_points")
        self.lineEdit_approk = QtWidgets.QLineEdit(Form)
        self.lineEdit_approk.setGeometry(QtCore.QRect(50, 190, 161, 31))
        self.lineEdit_approk.setObjectName("lineEdit_approk")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(50, 380, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(290, 350, 141, 28))
        self.pushButton_add.setObjectName("pushButton_add")
        self.label_graph_name = QtWidgets.QLabel(Form)
        self.label_graph_name.setGeometry(QtCore.QRect(40, 50, 151, 21))
        self.label_graph_name.setText("")
        self.label_graph_name.setObjectName("label_graph_name")
        self.checkBox_approk = QtWidgets.QCheckBox(Form)
        self.checkBox_approk.setGeometry(QtCore.QRect(60, 240, 141, 20))
        self.checkBox_approk.setObjectName("checkBox_approk")
        self.checkBox_teor = QtWidgets.QCheckBox(Form)
        self.checkBox_teor.setGeometry(QtCore.QRect(60, 330, 251, 20))
        self.checkBox_teor.setObjectName("checkBox_teor")
        self.checkBox_main_value = QtWidgets.QCheckBox(Form)
        self.checkBox_main_value.setGeometry(QtCore.QRect(170, 130, 221, 20))
        self.checkBox_main_value.setObjectName("checkBox_main_value")
        self.checkBox_integer = QtWidgets.QCheckBox(Form)
        self.checkBox_integer.setGeometry(QtCore.QRect(330, 310, 141, 20))
        self.checkBox_integer.setObjectName("checkBox_integer")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(390, 150, 131, 20))
        self.checkBox.setObjectName("checkBox")
        self.listWidget_graphics = QtWidgets.QListWidget(Form)
        self.listWidget_graphics.setGeometry(QtCore.QRect(290, 390, 256, 192))
        self.listWidget_graphics.setObjectName("listWidget_graphics")
        self.checkBox_differ = QtWidgets.QCheckBox(Form)
        self.checkBox_differ.setGeometry(QtCore.QRect(330, 270, 211, 20))
        self.checkBox_differ.setObjectName("checkBox_differ")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_show_graph.setText(_translate("Form", "Построить график"))
        self.pushButton_differ.setText(_translate("Form", "Пробный график"))
        self.pushButton_show.setText(_translate("Form", "Вывести график"))
        self.checkBox_points.setText(_translate("Form", "Только точки "))
        self.pushButton_cancel.setText(_translate("Form", "Сброс"))
        self.pushButton_add.setText(_translate("Form", "Добавить график"))
        self.checkBox_approk.setText(_translate("Form", "Аппроксимировать"))
        self.checkBox_teor.setText(_translate("Form", "Нанести теоретическую зависимость"))
        self.checkBox_main_value.setText(_translate("Form", "Построить основные занчения"))
        self.checkBox_integer.setText(_translate("Form", "Интегрировать"))
        self.checkBox.setText(_translate("Form", "Пробный график"))
        self.checkBox_differ.setText(_translate("Form", "Дифференцировать"))