HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        if summa > 0:
            kortti.lataa(summa)

    def osta_lounas(self, kortti):
        if kortti.saldo > 5:
            kortti.osta(5)
            self.myytyja_lounaita = self.myytyja_lounaita + 1

