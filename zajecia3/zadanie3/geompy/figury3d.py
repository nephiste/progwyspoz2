# geompy/figury3d.py

import math

# Funkcja do obliczania objętości i pola powierzchni sześcianu
def szescian(bok):
    objetosc = bok ** 3
    pole_powierzchni = 6 * bok ** 2
    return objetosc, pole_powierzchni

# Funkcja do obliczania objętości i pola powierzchni prostopadłościanu
def prostopadloscian(dlugosc, szerokosc, wysokosc):
    objetosc = dlugosc * szerokosc * wysokosc
    pole_powierzchni = 2 * (dlugosc * szerokosc + dlugosc * wysokosc + szerokosc * wysokosc)
    return objetosc, pole_powierzchni

# Funkcja do obliczania objętości i pola powierzchni kuli
def kula(promien):
    objetosc = (4 / 3) * math.pi * promien ** 3
    pole_powierzchni = 4 * math.pi * promien ** 2
    return objetosc, pole_powierzchni
