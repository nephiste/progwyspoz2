class Osoba:
    def __init__(self, imie: str, nazwisko: str, wiek: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}."

class Pracownik(Osoba):
    def __init__(self, imie: str, nazwisko: str, wiek: int, stanowisko: str, pensja: float):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł."

class Manager(Pracownik):
    def __init__(self, imie: str, nazwisko: str, wiek: int, stanowisko: str, pensja: float):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = []  # Lista podwładnych

    def dodaj_do_zespolu(self, pracownik: Pracownik):
        self.zespol.append(pracownik)

    def przedstaw_sie(self):
        # Rozszerzamy metodę przedstaw_sie, aby zawierała liczbę podwładnych
        liczba_podwladnych = len(self.zespol)
        return f"{super().przedstaw_sie()} Pracuję jako {self.stanowisko} i mam {liczba_podwladnych} podwładnych."

    def wyswietl_zespol(self):
        if not self.zespol:
            return "Brak pracowników w zespole."
        zespol_info = "\n".join([f"{pracownik.imie} {pracownik.nazwisko} - {pracownik.stanowisko}" for pracownik in self.zespol])
        return f"Zespół: \n{zespol_info}"

# tworzenie instancji Pracowników
pracownik1 = Pracownik("Jan", "Kowalski", 30, "Programista", 50000)
pracownik2 = Pracownik("Anna", "Nowak", 25, "Tester", 4000)

# tworzenie instancji Managera
manager = Manager("Marek", "Wiśniewski", 45, "Kierownik", 8000)

# dodawanie pracowników do zespołu
manager.dodaj_do_zespolu(pracownik1)
manager.dodaj_do_zespolu(pracownik2)

print(manager.przedstaw_sie())  # Manager przedstawia siebie z informacją o podwładnych
print(manager.info_o_pracy())   # Manager przedstawia swoje info o pracy
print(manager.wyswietl_zespol()) # Wyświetlenie zespołu managera

print(pracownik1.przedstaw_sie())  # Pracownik1 przedstawia siebie
print(pracownik2.info_o_pracy())  # Pracownik2 przedstawia informacje o pracy
