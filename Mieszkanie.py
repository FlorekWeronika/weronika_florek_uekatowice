class Mieszkanie:

    def __init__(self,
                ulica: str,
                numer_budynku: int,
                pietro: int,
                powierzchnia: float):
        self.ulica = ulica
        self.numer_budynku = numer_budynku
        self.pietro = pietro
        self.powierzchnia = powierzchnia

    @property
    def ulica(self) -> None:
        return self.ulica

    @property
    def numer_budynku(self) -> None:
        return self.numer_budynku

    @property
    def pietro(self) -> None:
        return self.pietro

    @property
    def powierzchnia(self) -> None:
        return self.powierzchnia

    def __str__(self):
        return f'Nazwa ulicy: {self.ulica},'\
               f'Numer budynku: {self.numer_budynku},'\
               f'Piętro na tórym znajduje się mieszkanie: {self.pietro},'\
               f'Powierzchnia mieszkania: {self.powierzchnia}.'