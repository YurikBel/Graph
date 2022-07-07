from UI_N_G_Window import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class N_G_Window(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_values.setColumnCount(4)
        self.table_values.setHorizontalHeaderLabels(['X', 'Y', 'Error X', 'Error Y'])
        self.buttonBox.accepted.connect(self.ok_click)
        self.pushButton_count.clicked.connect(self.do_table)
        self.checkBox_error.stateChanged.connect(self.err)
        self.checkBox.stateChanged.connect(self.logar)
        self.log = False
        self.err = False
        self.line_x_error.setText('None')
        self.line_y_error.setText('None')

    def do_table(self):
        count = int(self.line_count.text())
        self.table_values.setRowCount(count)

    def logar(self, state):
        if state == Qt.Checked:
            self.log = True
        else:
            self.log = False

    def err(self, state):
        if state == Qt.Checked:
            self.err = True
            for i in range(self.table_values.rowCount()):
                self.table_values.setItem(i, 2, QtWidgets.QTableWidgetItem(f'None'))
                self.table_values.setItem(i, 3, QtWidgets.QTableWidgetItem(f'None'))
        else:
            self.err = False

    def ok_click(self):
        name = self.line_name.text()
        x_name = self.line_x_name.text()
        y_name = self.line_y_name.text()
        x_err = self.line_x_error.text()
        y_err = self.line_y_error.text()
        log = self.log
        err = self.err
        with open(f'graphics/{name}.dat', 'w') as outfile:
            outfile.write(f'{x_name}, {y_name}, {x_err}, {y_err}, {log}, {err}\n')
            rows = self.table_values.rowCount()
            cols = self.table_values.columnCount()
            for row in range(rows):
                for col in range(cols):
                    if self.table_values.item(row, col) is not None:
                        outfile.write(f'{self.table_values.item(row, col).text()}  ')
                    else:
                        outfile.write(f'None  ')
                outfile.write('\n')



