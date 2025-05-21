from nagykonyv import Konyv

class Konyvtar:
    def __init__(self):
        self.konyvek = []
        self.fajl_beolvasas()

    def fajl_beolvasas(self):
        with open('konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
            next(forrasfajl)    
            for sor in forrasfajl:
                adatok = sor.strip().split(';')
                nev = adatok[0]
                szul_ev = int(adatok[1])
                hal_ev = int(adatok[2]) if adatok[2] else 2005
                nemzetiseg = adatok[3]
                cim = adatok[4]
                helyezes = int(adatok[5])

                self.konyvek.append(Konyv(nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes))

    def konyvek_db(self):
        print(len(self.konyvek))      
          
konyvtar = Konyvtar()       
for konyv in konyvtar.konyvek: 
    print(konyv.nev, konyv.cim)
# konyvtar.fajl_beolvasas