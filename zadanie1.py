import json


class ModelAI:
    licznik = 0

    def nowy_model(self):
        ModelAI.licznik += 1

    def __init__(self, version, name):
        self.nowy_model()
        self.version = version  # Poprawienie literówki z 'verison' na 'version'
        self.name = name

    @classmethod
    def ile_modeli(cls):
        return f"liczba utworzonych obiektów: {cls.licznik}"

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, "r") as f:
            data = json.load(f)  # Wczytanie danych JSON jako słownik

        # Odczytanie wartości 'name' i 'version' z danych JSON
        name = data.get("name")
        version = data.get("version")

        if name is None or version is None:
            raise ValueError("Plik JSON musi zawierać 'name' i 'version'.")

        return cls(version, name)


# Przykład użycia:
model1 = ModelAI.z_pliku("test.json")  # Wczytanie danych z pliku JSON
model2 = ModelAI("version2", "name2")  # Inny sposób tworzenia obiektu
model3 = ModelAI("version3", "name3")  # Kolejny sposób tworzenia obiektu

print(ModelAI.ile_modeli())  # Wyświetlenie liczby utworzonych obiektów
print(model1.version)  # Sprawdzamy wersję modelu wczytanego z pliku
print(model1.name)  # Sprawdzamy nazwę modelu wczytanego z pliku
