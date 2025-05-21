from nagykonyv import Konyv

class konyvtar:
    def __init__(self):
        self.konyvek = []
        self.fajl_beolvasás()

    def fajl_beolvasas(self):
        with open('konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
        next (forrasfajl)    
        for sor in forrasfajl:
            adatok = sor.strip().split(';')
            nev = adatok[0]
            szul_ev = int(adatok[1])
            hal_ev = int(adatok[2])
            nemzetiseg = adatok[3]
            cim = adatok[4]
            helyezes = int(adatok[5])

            self.konyvek.append(Konyv(nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes))