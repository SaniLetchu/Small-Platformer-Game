import unittest

from src.Pelaaja import player
from src.Kartta import Kartta1


class Test(unittest.TestCase):

    def test_luopelaajan_jatarkastaaliikkumisen(self):
        playerman = player()
        pelaajaolio = playerman.luopelaaja()
        (xalussa, yalussa) = playerman.location
        playerman.updatelocation(2, 5)
        playerman.updatelocation(4, -2)
        (x, y) = playerman.location
        self.assertEqual(xalussa + 2 + 4, x)
        self.assertEqual(yalussa + 5 - 2, y)

    def test_oikeamääräpalikoitakartassa(self):
        pelikenttä = Kartta1()
        self.assertEqual(188, len(pelikenttä.objects))




