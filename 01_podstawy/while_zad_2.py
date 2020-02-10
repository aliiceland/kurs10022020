"""
Napisz program, który bedzie przyjmowa od użytkownika liczby (input)
Jeśli wpiszemy k - to zakończy działanie pętli i wypisze średnią z podanych liczb

"""

i, suma = 0, 0

while True:
    wartosc = input("Podaj liczbę lub wpisz k by zakończyć: ")
    if wartosc == 'k':
        break
    i += 1
    suma += int(wartosc)

print(f"Średnia wartość wynosi: {suma / i:.2f}")

