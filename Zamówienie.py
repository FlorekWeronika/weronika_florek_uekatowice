class Zamowienie:

    def __init__(self,
                id_zamowienia: str,
                dane_klienta: str,
                cena: list,
                lokalizacja: str):
        self.id_zamowienia = id_zamowienia
        self.dane_klienta = dane_klienta
        self.cena = cena
        self.lokalizacja = lokalizacja

    @property
    def id_zamowienia(self) -> None:
        return self.id_zamowienia

    @id_zamowienia.setter
    def id_zamowienia(self, value: str):
        self.id_zamowienia = value


    @property
    def dane_klienta(self) -> None:
        return self.dane_klienta

    @dane_klienta.setter
    def dane_klienta(self, value: str):
        self.dane_klienta = value


    @property
    def cena(self) -> None:
        return self.cena

    @cena.setter
    def cena(self, value: list):
        self.cena = value

    @property
    def lokalizacja(self) -> None:
        return self.lokalizacja

    @lokalizacja.setter
    def lokalizacja(self, value: str):
        self.lokalizacja = value

    def __str__(self):
        return f'Numer zamówienia: {self.id_zamowienia},'\
               f'Dane klienta: {self.dane_klienta},'\
               f'Cena zamówienia: {self.cena},'\
               f'Lokalizacja: {self.lokalizacja}.'

    def sum_cena(self) -> float:
        kwota = 0
        for i in range(len(self.cena)):
            kwota = kwota + self.cena[i]
        return round(kwota, 2)