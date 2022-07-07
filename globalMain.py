from UImainWindow import Ui_MainWindow
import sys
import os
from N_G_Window import N_G_Window
from Laboratories.Holl.Graph_window import *
from graph_widget import Graph_widget


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_values.setColumnCount(4)
        self.table_values.setHorizontalHeaderLabels(['X', 'Y', 'Error X', 'Error Y'])
        self.action_create_graph.triggered.connect(self.create_graph)
        self.Grahps_list.currentItemChanged.connect(self.show_graph_values)
        self.pushButton.clicked.connect(self.show_graph)

    def show_graph(self):
        if self.Grahps_list.currentItem() is not None:
            name = self.Grahps_list.currentItem().text()
            window = Graph_widget(name)
            window.show()
            window.exec_()


    def show_graph_values(self):
        if self.Grahps_list.currentItem() is not None:
            name = self.Grahps_list.currentItem().text()
            self.label_graph_name.setText(f'{name}')
            self.table_values.setColumnCount(4)
            self.table_values.setHorizontalHeaderLabels(['X', 'Y', 'Error X', 'Error Y'])

            with open(f'graphics/{name}') as f:
                lines = f.read().splitlines()
                self.table_values.setRowCount(len(lines) - 1)
                for i in range(1, len(lines)):
                    val = lines[i].split()
                    x, y, x_e, y_e = val
                    self.table_values.setItem(i - 1, 0, QtWidgets.QTableWidgetItem(f'{x}'))
                    self.table_values.setItem(i - 1, 1, QtWidgets.QTableWidgetItem(f'{y}'))
                    self.table_values.setItem(i - 1, 2, QtWidgets.QTableWidgetItem(f'{x_e}'))
                    self.table_values.setItem(i - 1, 3, QtWidgets.QTableWidgetItem(f'{y_e}'))

    def fill_graphs(self):
        files = os.listdir('graphics')
        self.Grahps_list.clear()
        self.Grahps_list.addItems([f'{k}' for k in files])

    def create_graph(self):
        window = N_G_Window()
        res = window.exec_()
        if res == 1:
            self.fill_graphs()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.fill_graphs()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
