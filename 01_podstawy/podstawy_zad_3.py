"""
- Pobierz napis od użytkownika - przy pomocy funkcji input
- wypisz długość napisu
- Zamień napis na liczbę - co gdy się nie da?
- wypisz kwadrat tej liczby

"""

napis = input("Wpisz liczbę: ")

print("Długość", len(napis))
print("Długość {}".format(len(napis)))
print(f"Długość {len(napis)}")

# ask for permision
if napis.isnumeric():
    print(int(napis) ** 2) 

# bag for forgivenes
try:
    liczba = int(napis)
except ValueError:
    pass


print("Koniec")