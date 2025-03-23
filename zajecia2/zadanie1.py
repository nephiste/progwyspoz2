class Ksiazka:
    def __init__(self, tytul : str, autor : str, rok_wydania : int):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return f"tytul: {self.tytul}, autor: {self.autor}, rok wydania: {self.rok_wydania}"

class Ebook(Ksiazka):
    def __init__(self, tytul : str, autor : str, rok_wydania : int, rozmiar_pliku: int):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku
    def opis(self):
        return f"{super().opis()}, rozmiar pliku: {self.rozmiar_pliku} MB"

class Audibook(Ksiazka):
    def __init__(self, tytul : str, autor : str, rok_wydania : int, czas_trwania: float):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania
    def opis(self):
        return f"{super().opis()}, czas trwania: {self.czas_trwania} minut"

# Tworzenie obiektów
ksiazka = Ksiazka("W pustyni i w puszczy", "Henryk Sienkiewicz", 1911)
ebook = Ebook("Python dla początkujących", "Jan Kowalski", 2023, 5)
audiobook = Audibook("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997, 360)

# Wypisywanie opisów
print(ksiazka.opis())  # Opis książki
print(ebook.opis())    # Opis ebooka
print(audiobook.opis()) # Opis audiobooka