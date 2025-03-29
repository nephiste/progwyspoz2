# geompy/figury2d.py

import math

# Funkcja do obliczania pola i obwodu kwadratu
def kwadrat(bok):
    pole = bok ** 2
    obwod = 4 * bok
    return pole, obwod

# Funkcja do obliczania pola i obwodu prostokąta
def prostokat(dlugosc, szerokosc):
    pole = dlugosc * szerokosc
    obwod = 2 * (dlugosc + szerokosc)
    return pole, obwod

# Funkcja do obliczania pola i obwodu koła
def kolo(promien):
    pole = math.pi * promien ** 2
    obwod = 2 * math.pi * promien
    return pole, obwod
