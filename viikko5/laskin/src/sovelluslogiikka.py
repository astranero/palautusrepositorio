class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.previous = 0

    def miinus(self, arvo):
        self.previous = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.previous = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.previous = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
