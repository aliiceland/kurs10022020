"""
stworz tabliczke mnozenia - listę list 
dla liczb od 1 do 10

1. zrób przy pomocy pętli
2. zrób to samo przy pomocy wyrażenia listowego

"""

tabliczka = []

for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i * j)
    tabliczka.append(row)
print(tabliczka)


tabliczka = [[i*j for j in range(1, 11)] for i in range(1, 11)]
print(tabliczka)