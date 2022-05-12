from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsRectItem

class platforms(QtWidgets.QGraphicsPolygonItem):

    def __init__(self):
        super(platforms, self).__init__()
        self.color = QtGui.QColor(170,56,23)
        self.size = 30

    def create(self, x, y):
        olio = QGraphicsRectItem(x, y, self.size, self.size)
        olio.setBrush(self.color)
        return olio

class kuolema(QtWidgets.QGraphicsPolygonItem):

    def __init__(self):
        super(kuolema, self).__init__()
        self.color = QtGui.QColor(0,0,0)
        self.size = 30

    def create(self, x, y):
        olio = QGraphicsRectItem(x, y, self.size, self.size)
        olio.setBrush(self.color)
        return olio

class maali(QtWidgets.QGraphicsPolygonItem):

    def __init__(self):
        super(maali, self).__init__()
        self.color = QtGui.QColor(0,200,0)
        self.size = 30

    def create(self, x, y):
        olio = QGraphicsRectItem(x, y, self.size, self.size)
        olio.setBrush(self.color)
        return olio

class Tausta(QtWidgets.QGraphicsPolygonItem):

    def __init__(self):
        super(Tausta, self).__init__()
        self.color = QtGui.QColor(30,130,200)
        self.size = 1280

    def create(self, x, y):
        olio = QGraphicsRectItem(x, y, self.size, self.size)
        olio.setBrush(self.color)
        return olio
