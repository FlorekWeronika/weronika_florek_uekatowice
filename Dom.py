class Dom:

    def __init__(self,
                ulica: str,
                numer_budynku: int,
                liczba_pokoi: int,
                powierzchnia: float):
        self.ulica = ulica
        self.numer_budynku = numer_budynku
        self.liczba_pokoi = liczba_pokoi
        self.powierzchnia = powierzchnia

    @property
    def ulica(self) -> None:
        return self.ulica

    @property
    def numer_budynku(self) -> None:
        return self.numer_budynku

    @property
    def liczba_pokoi(self) -> None:
        return self.liczba_pokoi

    @property
    def powierzchnia(self) -> None:
        return self.powierzchnia

    def __str__(self):
        return f'Nazwa ulicy: {self.ulica},'\
               f'Numer budynku: {self.numer_budynku},'\
               f'Liczba pokoi w domu: {self.liczba_pokoi},'\
               f'Powierzchnia domu: {self.powierzchnia}.'