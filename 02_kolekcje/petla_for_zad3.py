"""
W zadanej liscie zamien element najmniejszy z najwiekszym
"""

lista = [10, 1, 3, 17, 4, 8, 25, 2]

# przekształcenia
lista[6] = 1
lista[1] = 25

assert lista == [10, 25, 3, 17, 4, 8, 1, 2]