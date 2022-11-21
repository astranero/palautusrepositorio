from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = {}
        self.tavaroiden_maara = 0
        self.yhteenlaskettu_hinta = 0
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.tavaroiden_maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.yhteenlaskettu_hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        
        if lisattava.nimi() in self.ostoskori:
            self.ostoskori[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            self.ostoskori[lisattava.nimi()] = Ostos(lisattava)

        self.tavaroiden_maara += 1
        self.yhteenlaskettu_hinta += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        if poistettava.nimi() in self.ostoskori:
            self.ostoskori[poistettava.nimi()].muuta_lukumaaraa(-1)
            if self.ostoskori[poistettava.nimi()].lukumaara() == 0:
                del self.ostoskori[poistettava.nimi()]

    def tyhjenna(self):
        self.ostoskori = {}

    def ostokset(self):
        return list(self.ostoskori.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
