"""
Napisz kod, który na podstawie wprowadzonych wymiarów
opakowania (prostopadłościan)
obliczy i sprawdzi, czy objętość jest większa od 1 litra (1000)

"""

a, b, h = 10, 10, 15

objetosc = a * b * h

if objetosc > 1000:
    print("Tak, większe niż litr")

elif objetosc >  2000:
    print("Więcej niż 2 litry")
else:
    print("Mniejsze")


