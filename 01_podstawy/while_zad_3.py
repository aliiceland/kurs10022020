"""
Z podanych w petli liczb
wybierz najmniejsza i największą
k kończy pętlę

x = None

"""

min_ = None
max_ = None

while True:
    value = input("Podaj liczbę lub k by zakończyć: ")
    if value == 'k':
        break
    value = int(value)
    if min_ is None or value < min_:
        min_ = value

    if max_ is None or value > max_:
        max_ = value

print(f"Max: {max_} , Min: {min_}") 
