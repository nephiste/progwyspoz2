class Osoba:
    def __init__(self, imie: str, nazwisko: str, wiek: int ):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}."

class Pracownik(Osoba):
    def __init__(self, imie: str, nazwisko: str, wiek: int, stanowisko: str, pensja: float ):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł."

class Manager(Pracownik):
    def __init__(self, imie: str, nazwisko: str, wiek: int, stanowisko: str, pensja: float ):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = []

    def dodaj_do_zespolu(self, Pracownik: pracownik):
        self.zespol.append(Pracownik)