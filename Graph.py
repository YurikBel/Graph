import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import math

import numpy as np


class Graph(ABC):
    def __init__(self, name, x_value, y_value, log, err):
        self.name = name
        self.x_value = x_value
        self.y_value = y_value
        self.log = log
        self.err = err

    @abstractmethod
    def build_graph(self, other):
        pass


class Graph_not_err(Graph):
    def __init__(self, name, x_value, y_value, log, err):
        super().__init__(name, x_value, y_value, log, err)

    def show(self):
        plt.show()

    def build_graph(self, other):
        if other:
            arr = []
            for k in self.y_value:
                arr.append(k ** (-1))
            plt.plot(self.x_value, arr, 'o')
        else:
            plt.plot(self.x_value, self.y_value)
        if self.log == 'True':
            plt.xscale('log')
        plt.minorticks_on()
        plt.grid(which='major',
                 color='k',
                 linewidth=0.5)
        plt.grid(which='minor',
                 color='k',
                 linestyle=':')

    def build_other(self):
        x = np.linspace(0, 4000, 3000)
        e = 0.213
        l = 0.107
        r = 85
        w = x * 2 * np.pi
        c = 34.3 * (0.1 ** 9)
        y1 = (e * w * l) / (np.sqrt(r ** 2 + ((w * l) - (1 / (w * c))) ** 2))
        y2 = (e * r)/ (np.sqrt(r ** 2 + ((w * l) - (1 / (w * c))) ** 2))
        y3 = e / ((np.sqrt(r ** 2 + ((w * l) - (1 / (w * c))) ** 2)) * w * c)
        y4 = np.pi * x * np.sqrt(c/l)
        y5 = 1000 * 2 * l / (x + 43)

        # y = (4 * (e ** 2) * (1720 * x - x**2)) / (1720 * la)
        # plt.plot(x, y1)
        plt.plot(x, y2)
        # plt.plot(x, y3)
        #plt.plot(x, y5)
        plt.plot(0, 0)
        plt.minorticks_on()
        plt.grid(which='major',
                 color='k',
                 linewidth=0.5)
        plt.grid(which='minor',
                 color='k',
                 linestyle=':')
class Graph_global_err(Graph):
    def __init__(self, name, x_value, y_value, log, err, x_err, y_err):
        super().__init__(name, x_value, y_value, log, err)
        self.x_err = x_err
        self.y_err = y_err

    def build_graph(self, other):
        if other:
            plt.errorbar(self.x_value, self.y_value, xerr=self.x_err, yerr=self.y_err, fmt='o', ecolor='red')
        else:
            plt.errorbar(self.x_value, self.y_value, xerr=self.x_err, yerr=self.y_err, fmt='o-', ecolor='red')
        if self.log == 'True':
            plt.xscale('log')
        plt.minorticks_on()
        plt.grid(which='major',
                 color='k',
                 linewidth=0.5)
        plt.grid(which='minor',
                 color='k',
                 linestyle=':')


    def show(self):
        plt.show()

class Graph_local_err(Graph):
    def __init__(self, name, x_value, y_value, log, err, x_err_value, y_err_value):
        super().__init__(name, x_value, y_value, log, err)
        self.x_err_value = [float(k) for k in x_err_value]
        self.y_err_value = [float(k) for k in y_err_value]

    def build_graph(self, other):
        if other:
            plt.errorbar(self.x_value, self.y_value, xerr=self.x_err_value, yerr=self.y_err_value, fmt='o', ecolor='red')
        else:
            plt.errorbar(self.x_value, self.y_value, xerr=self.x_err_value, yerr=self.y_err_value, fmt='o-', ecolor='red')
        if self.log == 'True':
            plt.xscale('log')
        plt.minorticks_on()
        plt.grid(which='major',
                 color='k',
                 linewidth=0.5)
        plt.grid(which='minor',
                 color='k',
                 linestyle=':')


    def show(self):
        plt.show()

class TransitGraph():
    def __init__(self, graph):
        self.graph = graph
        self.approk = False
        self.differ = False
        self.integer = False
        self.points = False
        self.name = None


    def build_graph(self):
        self.graph.build_graph(self.points)
