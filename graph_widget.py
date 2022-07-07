from UIgraph_widget import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from repository import *
from Transit_graph import *


class Graph_widget(Ui_Form, QtWidgets.QDialog):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.label_graph_name.setText(name)
        self.graph = Repository().create(name)
        self.points = False
        self.diff = False
        self.integer = False
        self.test = False
        self.approk = None
        self.teor = None
        self.main_value = True
        self.list_graph = []
        self.checkBox_points.stateChanged.connect(self.points_on)
        self.pushButton_show_graph.clicked.connect(self.show_graph)
        self.pushButton_cancel.clicked.connect(self.clear)
        self.pushButton_differ.clicked.connect(self.other)
        self.pushButton_show.clicked.connect(self.vieu)
        self.pushButton_add.clicked.connect(self.add_transit)

    def fill_list_transit(self):
        self.listWidget_graphics.clear()
        self.listWidget_graphics.addItems([f'{k.name}' for k in self.list_graph])

    def add_transit(self):
        window = Transit_graph()
        window.fill_graphs()
        res = window.exec_()
        if res == 1:
            transit_graph = window.root_graph
            self.list_graph.append(transit_graph)
            self.fill_list_transit()
            # создавать объект транзитный график и засовывать его в поле граф виджет
            # вызывать функцию обновления листа добавленных графиков



    def vieu(self):
        self.graph.show()

    def other(self):
        self.graph.build_other()

    def points_on(self, state):
        if state == Qt.Checked:
            self.points = True
        else:
            self.points = False

    def clear(self):
        self.graph.clear()

    def show_graph(self):
        self.graph.build_graph(self.points)
        for graph in self.list_graph:
            graph.build_graph()