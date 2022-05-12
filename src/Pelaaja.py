from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsRectItem

class player(QtWidgets.QGraphicsPolygonItem):

    def __init__(self):
        super(player, self).__init__()
        self.color = QtGui.QColor(0, 0, 200)
        self.pelaajaolio = None
        self.location = (1, 607)

    def luopelaaja(self):
        self.pelaajaolio = QGraphicsRectItem(1, 607, 30, 30)
        self.pelaajaolio.setBrush(self.color)
        return self.pelaajaolio

    def updatelocation(self, xmuutos ,ymuutos):
        (nykyinenx, nykyineny) = self.location
        y = nykyineny + ymuutos
        x = nykyinenx + xmuutos
        self.location = (x, y)