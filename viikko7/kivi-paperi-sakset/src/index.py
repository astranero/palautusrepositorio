from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def luo_peli(tyyppi):
    vaikeustaso = {
        "a": KPSPelaajaVsPelaaja(),
        "b": KPSTekoaly(),
        "c": KPSParempiTekoaly(),
    }
    return vaikeustaso[tyyppi]


def main():
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()
        try:
            peli = luo_peli(vastaus)
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli.pelaa()
        except KeyError:
            break


if __name__ == "__main__":
    main()
