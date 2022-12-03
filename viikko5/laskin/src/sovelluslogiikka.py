class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.historia =  []

    def miinus(self, arvo):
        self.historia.append(self.tulos)
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.historia.append(self.tulos)
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.historia.append(self.tulos)
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        arvo = self.historia.pop()
        self.aseta_arvo(arvo)