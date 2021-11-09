#zad.1
class FirmaTransportowa:
    def __init__(self, kurs, pojazd, odcinek, FirmaSpozywcza):
        self.kurs = kurs
        self.pojazd = pojazd
        self.odcinek = odcinek
        self.FirmaSpozywcza = FirmaSpozywcza

    @property
    class kurs:
        def kurs(self, dystnas, pojazd, miejsce_rozpoczecia, miejsce_zakonczenia, id_kierowcy ):
            self.dystans = pojazd
            self.pojazd = pojazd
            self.miejsce_rozpoczecia = miejsce_rozpoczecia
            self.miejsce_zakonczenia = miejsce_zakonczenia
            self.id_kierowcy = id_kierowcy


    @property
    class pojazd:
        def __init__(self, marka, rok, przebieg, rodzajpaliwa, pojemnosc_silnika):
            self.marka = marka
            self.rok = rok
            self.przebieg = przebieg
            self.rodzajpaliwa = rodzajpaliwa
            self.pojemnosc_silnika = pojemnosc_silnika

    @property
    class odcinek:
        def __init__(self, odleglosc, miejsce_rozpoczecia, miejsce_zakonczenia, pojazd, FirmaSpozywcza):
            self.odleglosc = odleglosc
            self.miejsce_rozpoczecia = miejsce_rozpoczecia
            self.miejsce_zakonczenia = miejsce_zakonczenia
            self.pojazd = pojazd
            self.Firmaspozywcza = FirmaSpozywcza

    @property
    class FirmaSpozywcza:
        def __init__(self, nazwa, rok, produkty, ilosc, dystans):
            self.nazwa = nazwa
            self.rok = rok
            self.produkty = produkty
            self.ilosc = ilosc
            self.dystans = dystans
