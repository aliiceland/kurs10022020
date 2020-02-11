"""
range(0, 101, 2)
len()

Napisz program, który będzie zliczał liczbę unikalnych liczb wprowadzanych przez użytkownika
Zliczanie kończy sie gdy użytkownik wpisze 'k'

W podsumowaniu napisz jak duż z podanych liczba to liczby parzyste z zakresu 0-200

"""
liczby = set()
while True:
    opcja = input("Podaj liczbę lub k: ")
    if opcja == "k":
        break
    
    liczby.add(int(opcja))

print(f"Unikalnych liczba: {len(liczby)}")
print(f"Parzystych z zakresu 0-200 {len(liczby & set(range(0, 201, 2)))}")