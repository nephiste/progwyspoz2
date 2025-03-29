# main.py

from geompy.figury2d import kwadrat, prostokat, kolo
from geompy.figury3d import szescian, prostopadloscian, kula

# Przykład obliczeń dla figur 2D
print("Kwadrat:")
bok = 4
pole, obwod = kwadrat(bok)
print(f'Pole: {pole}, Obwód: {obwod}')

print("\nProstokąt:")
dlugosc, szerokosc = 5, 3
pole, obwod = prostokat(dlugosc, szerokosc)
print(f'Pole: {pole}, Obwód: {obwod}')

print("\nKoło:")
promien = 7
pole, obwod = kolo(promien)
print(f'Pole: {pole}, Obwód: {obwod}')

# Przykład obliczeń dla figur 3D
print("\nSześcian:")
bok = 3
objetosc, pole_powierzchni = szescian(bok)
print(f'Objętość: {objetosc}, Pole powierzchni: {pole_powierzchni}')

print("\nProstopadłościan:")
dlugosc, szerokosc, wysokosc = 6, 4, 2
objetosc, pole_powierzchni = prostopadloscian(dlugosc, szerokosc, wysokosc)
print(f'Objętość: {objetosc}, Pole powierzchni: {pole_powierzchni}')

print("\nKula:")
promien = 5
objetosc, pole_powierzchni = kula(promien)
print(f'Objętość: {objetosc}, Pole powierzchni: {pole_powierzchni}')
