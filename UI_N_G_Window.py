# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'N_G_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(996, 702)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(540, 470, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.table_values = QtWidgets.QTableWidget(Dialog)
        self.table_values.setGeometry(QtCore.QRect(10, 20, 431, 621))
        self.table_values.setObjectName("table_values")
        self.table_values.setColumnCount(0)
        self.table_values.setRowCount(0)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(630, 90, 61, 31))
        self.label.setObjectName("label")
        self.line_name = QtWidgets.QLineEdit(Dialog)
        self.line_name.setGeometry(QtCore.QRect(710, 90, 171, 31))
        self.line_name.setObjectName("line_name")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(650, 160, 61, 31))
        self.label_3.setObjectName("label_3")
        self.line_x_name = QtWidgets.QLineEdit(Dialog)
        self.line_x_name.setGeometry(QtCore.QRect(710, 160, 171, 31))
        self.line_x_name.setObjectName("line_x_name")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(650, 210, 61, 31))
        self.label_2.setObjectName("label_2")
        self.line_y_name = QtWidgets.QLineEdit(Dialog)
        self.line_y_name.setGeometry(QtCore.QRect(710, 210, 171, 31))
        self.line_y_name.setObjectName("line_y_name")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(490, 260, 211, 31))
        self.label_4.setObjectName("label_4")
        self.line_x_error = QtWidgets.QLineEdit(Dialog)
        self.line_x_error.setGeometry(QtCore.QRect(710, 260, 171, 31))
        self.line_x_error.setObjectName("line_x_error")
        self.line_y_error = QtWidgets.QLineEdit(Dialog)
        self.line_y_error.setGeometry(QtCore.QRect(710, 310, 171, 31))
        self.line_y_error.setObjectName("line_y_error")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(490, 310, 211, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(460, 360, 541, 20))
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(710, 400, 181, 20))
        self.checkBox.setObjectName("checkBox")
        self.line_count = QtWidgets.QLineEdit(Dialog)
        self.line_count.setGeometry(QtCore.QRect(710, 20, 113, 22))
        self.line_count.setObjectName("line_count")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(590, 20, 111, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton_count = QtWidgets.QPushButton(Dialog)
        self.pushButton_count.setGeometry(QtCore.QRect(720, 50, 101, 28))
        self.pushButton_count.setObjectName("pushButton_count")
        self.checkBox_error = QtWidgets.QCheckBox(Dialog)
        self.checkBox_error.setGeometry(QtCore.QRect(710, 430, 151, 20))
        self.checkBox_error.setObjectName("checkBox_error")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "????????????????:"))
        self.label_3.setText(_translate("Dialog", "?????? ??:"))
        self.label_2.setText(_translate("Dialog", "?????? Y:"))
        self.label_4.setText(_translate("Dialog", "?????????????????????????? ?????????????????????? ???? X:"))
        self.label_5.setText(_translate("Dialog", "?????????????????????????? ?????????????????????? ???? Y:"))
        self.label_6.setText(_translate("Dialog", "(?????????????????????????? ?????????????????????? ?????????????? ???????????? ???????? ?????????????? ???????????????????????? X ?? Y ????????????)"))
        self.checkBox.setText(_translate("Dialog", "?????????????????????????????? ?????? X"))
        self.label_7.setText(_translate("Dialog", "???????????????????? ??????????:"))
        self.pushButton_count.setText(_translate("Dialog", "???????????? ??????-????"))
        self.checkBox_error.setText(_translate("Dialog", "?????? ????????????????????????"))
