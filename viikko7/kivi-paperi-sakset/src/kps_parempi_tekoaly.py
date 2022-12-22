from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self):
        # metodin oletustoteutus
        return self.tekoaly.anna_siirto()
