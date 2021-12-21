import self as self


class Developer:

    def __init__(self,
                 nazwa: str,
                 liczba_klientow: int,
                 liczba_mieszkan: int,
                 liczba_domow: int):
        self.nazwa = nazwa
        self.liczba_klientow = liczba_klientow
        self.liczba_mieszkan = liczba_mieszkan
        self.liczba_domow = liczba_domow

    @property
    def nazwa(self) -> None:
        return self.nazwa


    @property
    def liczba_klientow(self) -> None:
        return self.liczba_klientow

    @property
    def liczba_mieszkan(self) -> None:
        return self.liczba_mieszkan

    @property
    def liczba_domow(self) -> None:
        return self.liczba_domow


    def __str__(self):
        return f'Nazwa firmy: {self.nazwa},'\
               f'Liczba klientów: {self.liczba_klientow},'\
               f'Liczba posiadanych mieszkań: {self.liczba_mieszkan},'\
               f'Liczba posiadanych domów: {self.liczba_domow}.'