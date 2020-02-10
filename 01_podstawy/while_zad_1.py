"""
Korzystajc z pętli while wypisz dla 100 pierwszych liczb parzystych
tę liczbę, jej kwadrat i sześcian. Zrob krok co 1
Jeśli liczba jest równa 33 to tez ją wypisz

print(f'{i},{i**2},{i**3}')
2, 4, 8

"""

i = 0

while i <= 100:
    if i % 2 == 0 or i == 33:
        print(f"{i:7},{i**2:7},{i**3:9}")
    i += 1