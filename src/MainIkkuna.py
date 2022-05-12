import sys
from PyQt5.QtCore import Qt
from Pelaaja import player
from src.Kartta import Kartta1
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

class PeliIkkuna(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)
        self.title = "Platformer"
        self.pelikenttä = Kartta1()
        self.width = 1280
        self.height = 720
        self.maassa = False
        self.vainkerran = 0
        self.koko = 30
        self.muoto = 1
        self.monesko = 0
        self.vauhtialas = 0
        self.initUI()
        self.loadmap()
        self.loadplayer()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.voitto)
        self.timer.timeout.connect(self.powerup)
        self.timer.timeout.connect(self.kuolema)
        self.timer.timeout.connect(self.gravity)


        self.timer.start(30)  # Milliseconds

    def initUI(self):
        print("You can move with AQWED keys")
        print("Get to the green finish line. Don't fall into the abyss!")
        print("Game can be closed by pressing Escape")
        print("Enjoy the game!")
        self.setWindowTitle(self.title)
        self.setFixedSize(1280, 720)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1260, 700)

        self.view = QtWidgets.QGraphicsView(self.scene, self)

        self.horizontal.addWidget(self.view)
        self.show()

    def loadmap(self):
        for i in self.pelikenttä.objects:
            self.scene.addItem(i)

    def loadplayer(self):
        self.playerman = player()
        self.hahmo = self.playerman.luopelaaja()
        self.scene.addItem(self.hahmo)

    def keyPressEvent(self, e):
        (nykyinenx, nykyineny) = self.playerman.location
        if e.key() == Qt.Key_Escape:
            print("See you next time!")
            sys.exit(app.exec())
        if e.key() == Qt.Key_D:
            if self.törmäys(nykyinenx + 3, nykyineny) == True:
                self.hahmo.moveBy(3, 0)
                self.playerman.updatelocation(3, 0)
            elif self.törmäys(nykyinenx + 2, nykyineny) == True:
                self.hahmo.moveBy(2, 0)
                self.playerman.updatelocation(2, 0)
            elif self.törmäys(nykyinenx + 1, nykyineny) == True:
                self.hahmo.moveBy(1, 0)
                self.playerman.updatelocation(1, 0)

        if e.key() == Qt.Key_A:
            if self.törmäys(nykyinenx - 3, nykyineny) == True:
                self.hahmo.moveBy(-3, 0)
                self.playerman.updatelocation(-3, 0)
            elif self.törmäys(nykyinenx - 2, nykyineny) == True:
                self.hahmo.moveBy(-2, 0)
                self.playerman.updatelocation(-2, 0)
            elif self.törmäys(nykyinenx - 1, nykyineny) == True:
                self.hahmo.moveBy(-1, 0)
                self.playerman.updatelocation(-1, 0)

        if e.key() == Qt.Key_E:
            if self.maassa == True:
                self.vauhtialas = -9
                self.maassa = False
            else:
                pass
            if self.törmäys(nykyinenx + 3, nykyineny) == True:
                self.hahmo.moveBy(3, 0)
                self.playerman.updatelocation(3, 0)
            elif self.törmäys(nykyinenx + 2, nykyineny) == True:
                self.hahmo.moveBy(2, 0)
                self.playerman.updatelocation(2, 0)
            elif self.törmäys(nykyinenx + 1, nykyineny) == True:
                self.hahmo.moveBy(1, 0)
                self.playerman.updatelocation(1, 0)


        if e.key() == Qt.Key_Q:
            if self.maassa == True:
                self.vauhtialas = -9
                self.maassa = False
            else:
                pass
            if self.törmäys(nykyinenx - 3, nykyineny) == True:
                self.hahmo.moveBy(-3, 0)
                self.playerman.updatelocation(-3, 0)
            elif self.törmäys(nykyinenx - 2, nykyineny) == True:
                self.hahmo.moveBy(-2, 0)
                self.playerman.updatelocation(-2, 0)
            elif self.törmäys(nykyinenx - 1, nykyineny) == True:
                self.hahmo.moveBy(-1, 0)
                self.playerman.updatelocation(-1, 0)


        if e.key() == Qt.Key_S:
            (x, y) = self.playerman.location
            if x >= 410:
                if y <= 60:
                    if self.muoto == 1:
                        self.hahmo.setRect(1, 607, 10, 10)
                        self.koko = 10
                        self.muoto = 0

        if e.key() == Qt.Key_W:
            if self.maassa == True:
                self.vauhtialas = -9
                self.maassa = False
            else:
                pass

    def mousePressEvent(self, QMouseEvent):
        self.monesko = self.monesko + 1
        if self.monesko == 4:
            print("Clicking does nothing.")
        if self.monesko == 8:
            print("Only controls you need are keys: AQWED")
        if self.monesko == 16:
            print("STOP IT!")
        if self.monesko >= 30:
            print("CLICK")

    def törmäys(self, mentäväx, mentäväy):
        for i in self.pelikenttä.varattu:
            (x, y) = i
            if x - self.koko <= mentäväx <= x + 30:
                if y - self.koko <= mentäväy <= y + 30:
                    return False
        return True

    def gravity(self):
        (x, y) = self.playerman.location
        if self.maassa == True:
            self.vauhtialas = 0
            #nomorejesus walking
            if self.törmäys(x, y + 1) == True:
                self.maassa = False
            pass
        else:
            self.vauhtialas = self.vauhtialas + 0.5
            if self.törmäys(x, y + self.vauhtialas) == True:
                self.hahmo.moveBy(0, self.vauhtialas)
                self.playerman.updatelocation(0, self.vauhtialas)
            else:
                self.maassa = True
                self.maahanmeno = self.vauhtialas
                self.maahan()

    def maahan(self):
        while True:
            (x, y) = self.playerman.location
            self.maahanmeno = self.maahanmeno - 0.5
            if self.maahanmeno <= 0:
                break
            if self.törmäys(x, y + self.maahanmeno) == True:
                self.hahmo.moveBy(0, self.maahanmeno)
                self.playerman.updatelocation(0, self.maahanmeno)

    def powerup(self):
        (x,y) = self.playerman.location
        if x >= 410:
            if y <= 60:
                if self.vainkerran == 0:
                    print("This altitude...Ahh...You feel new power surging in you. Maybe try pressing key S?")
                    self.vainkerran = 1

    def voitto(self):
        (x, y) = self.playerman.location
        if x >= 1192:
            if y <= 60:
                print("You have won!")
                sys.exit(app.exec())

    def kuolema(self):
        (x, y) = self.playerman.location
        if y >= 649:
            print("You have lost. Better luck next time!")
            sys.exit(app.exec())

class MainIkkuna(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Platformer"
        self.width = 120
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(1280, 720, self.width, self.height)

        Pelaa = QPushButton("Play", self)
        Pelaa.move(23, 20)
        Pelaa.clicked.connect(self.Play)

        Poistu = QPushButton("Exit", self)
        Poistu.move(23, 50)
        Poistu.clicked.connect(self.Exit)

        self.show()

    @pyqtSlot()
    def Play(self):
        self.lmao = PeliIkkuna()
        self.close()

    @pyqtSlot()
    def Exit(self):
        sys.exit(app.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainIkkuna()
    sys.exit(app.exec())
