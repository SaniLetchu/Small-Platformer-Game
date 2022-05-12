from src.Esine import kuolema
from src.Esine import platforms
from src.Esine import maali
from src.Esine import Tausta

class Kartta1():

    def __init__(self):
        self.name = "kartta1"
        self.objects = []
        self.varattu = []
        self.palikka = platforms()
        self.kuolema = kuolema()
        self.maali = maali()
        self.tausta = Tausta()


        self.constructmap()

    def constructmap(self):
        #tausta
        self.luotausta(1, 0, 0)

        #kuolemataso
        self.luotasojakuolema(42, 0, 670)

        # luomaali
        self.luotasojamaali(2, 1200, 0)
        self.luotasojamaali(2, 1200, 30)

        #alhaalla muokattavaa ylhäällä lopulliset

        #luomaataso
        file = open("kartta1", "r")
        for line in file:
            jaettu = line.split(",")
            tyhjälista = []
            for i in jaettu:
                yksivaihe = i.split()
                yksiasia = yksivaihe[0]
                tyhjälista.append(yksiasia)
            if tyhjälista[0] == "seina":
                self.luoseiniä(int(tyhjälista[1]), int(tyhjälista[2]), int(tyhjälista[3]))
            elif tyhjälista[0] == "taso":
                self.luotasoja(int(tyhjälista[1]), int(tyhjälista[2]), int(tyhjälista[3]))
        file.close()


    def luotasojakuolema(self, monta, xtaso, ytaso):
        for i in range(0, monta):
            lasku = 30 * i
            tämä = lasku + xtaso
            jotain = self.kuolema.create(tämä, ytaso)
            self.objects.append(jotain)

    def luotasoja(self, monta, xtaso, ytaso):
        for i in range(0, monta):
            lasku = 30 * i
            tämä = lasku + xtaso
            jotain = self.palikka.create(tämä, ytaso)
            self.varattu.append((tämä, ytaso))
            self.objects.append(jotain)

    def luotasojamaali(self, monta, xtaso, ytaso):
        for i in range(0, monta):
            lasku = 30 * i
            tämä = lasku + xtaso
            jotain = self.maali.create(tämä, ytaso)
            self.objects.append(jotain)

    def luoseiniä(self, monta, xtaso, ytaso):
        for i in range(0, monta):
            lasku = 30 * i
            tämä = ytaso - lasku
            jotain = self.palikka.create(xtaso, tämä)
            self.varattu.append((xtaso, tämä))
            self.objects.append(jotain)

    def luotausta(self, monta, xtaso, ytaso):
        for i in range(0, monta):
            lasku = 30 * i
            tämä = lasku + xtaso
            jotain = self.tausta.create(tämä, ytaso)
            self.objects.append(jotain)








