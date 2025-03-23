class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent

class Modul_Komunikacji:
    def wyslij_wiadomosc(self, odbiorca, tresc):
        return f"Wyslano {tresc} do {odbiorca}"

class Modul_Rozrywki:
    def odwtorz_muzyke(self, utwor):
        return f"Leci piosenka {utwor}"

class Smartfon(Telefon):
    def __init__(self, model, producent):
        super().__init__(model, producent)
        self.komunikacja = Modul_Komunikacji()
        self.rozrywka = Modul_Rozrywki()

    def wyslij_wiadomosc(self, odbiorca, tresc):
        return self.komunikacja.wyslij_wiadomosc(odbiorca, tresc)

    def odwtorz_muzyke(self, utwor):
        return self.rozrywka.odwtorz_muzyke(utwor)

smartfon = Smartfon("Pixel 8", "Google")
print(smartfon.wyslij_wiadomosc("Werka", "Kup bułki po drodzę z pracy"))
print(smartfon.odwtorz_muzyke("Rick Astley - Never Gonna Give You Up"))