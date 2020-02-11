
a = {3, 2, 1}

b = set([3, 4, 5])

c = {1,1,1,1,2,2,2,3,3}
c.add(4)  # doda element do zbioru. Nie ma tu kolejnosci
print(c)
print(a)

print(a | b)  # suma zbiorow
print(a - b)  # różnica
print(a & b)  # część wspólna, iloczyn
print(a ^ b)  # róznica symetryczna. Są w a lub b ale nie w ich iloczynie

print(set([1, 1, 2, 2, 3, 3]))
print(set((1, 1, 2, 2, 3, 3)))
print(set("ala ma kota"))

# pust zbior to set() a nie {}

print(set(
    {"a": 1, "b": 2}
))