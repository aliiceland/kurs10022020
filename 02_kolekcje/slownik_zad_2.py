"""
Napisz program, który:
- wypisze dostępne produkty (oraz ich ceny). Produkty te powinny się znajdować w słowniku
- na podstawie dialogu z użytkownikiem wylicz cenę za wybrany towar. 

np. 

Oferujemy:

<lista produktów>: <cena> PLN

Co chcesz kupić? ziemniaki
Ile chcesz kupić [ziemniaki]? 5

Do zapłaty: 15 PLN

"""

produkty = {
    "marchew": 1.99,
    "zieminiaki": 2.14,
    "pomidory": 3,
}

magazyn = {
    "marchew": 10,
    "zieminiaki": 10,
    "pomidory": 10,
}

while True:
    opcja = input("Zakup [z] czy magazyn [m], koniec [k]")
    if opcja == "k":
        break
    elif opcja == "z":

        print("Oferujemy: ")
        for k, v in produkty.items():
            print(f" - {k} w cenie: {v}/kg")

        print()
        produkt = input("Co chcesz kupić? ")

        ile = float(input(f"Ile kg chcesz kupić [{produkt}]? "))

        cena_za_kg = produkty.get(produkt)
        # if cena_za_kg is None
        if not cena_za_kg:
            print("Nie mamy takiego produktu")
        elif ile > magazyn[produkt]:
            print("Nie mamy tyle!!")
        else:
            koszt = cena_za_kg * ile
            print(f"Do zapłaty: {koszt}")
            magazyn[produkt] = magazyn.get(produkt) - ile
    
    elif opcja == "m":

        produkt = input("Co chcesz dodać? ")
        ile = float(input(f"Ile chcesz dodać [{produkt}]? "))

        if produkt in produkty:
            magazyn[produkt] += ile
        else:
            magazyn[produkt] = ile
            cena = float(input("Cena za kg? "))
            produkty[produkt] = cena
