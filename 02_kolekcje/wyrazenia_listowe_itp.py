# utworz liste zawierajacą liczbe i jej sześcian z zakresu od 0 do 100
# jeżeli to są liczby podzielne przez 5

liczby = []
for i in range(101):
    if i % 5 == 0:
        liczby.append([i, i**3])

print(liczby)

liczby = [[i, i**3] for i in range(101) if i % 5 == 0]
print(liczby)

# utworzyc slownik ktoru zawiera takie pary jak powyżej

liczby = {i: i**3 for i in range(101) if i % 5 == 0}
print(liczby)

# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, ...]]

kolekcja = (i for i in range(10))
print(kolekcja)
print(tuple(kolekcja))