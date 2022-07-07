from UITransit_graph import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from repository import *
import os


class Transit_graph(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.root_graph = None
        self.listWidget_all_graphs.currentItemChanged.connect(self.refresh_root_graph)
        self.checkBox_points.stateChanged.connect(self.points_on)
        self.approk = False
        self.differ = False
        self.integer = False
        self.points = False

    def points_on(self, state):
        if state == Qt.Checked:
            self.points = True
        else:
            self.points = False
        if self.root_graph is not None:
            self.root_graph.points = self.points


    def fill_graphs(self):
        files = os.listdir('graphics')
        self.listWidget_all_graphs.clear()
        self.listWidget_all_graphs.addItems([f'{k}' for k in files])

    def refresh_root_graph(self):
        if self.listWidget_all_graphs.currentItem() is not None:
            name = self.listWidget_all_graphs.currentItem().text()
            graph = Repository().create(name)
            self.root_graph = TransitGraph(graph)
            self.root_graph.name = name
            self.root_graph.approk = self.approk
            self.root_graph.differ = self.differ
            self.root_graph.integer = self.integer
            self.root_graph.points = self.points

