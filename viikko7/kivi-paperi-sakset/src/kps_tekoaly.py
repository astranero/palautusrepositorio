from tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self):
        # metodin oletustoteutus
        return self.tekoaly.anna_siirto()
