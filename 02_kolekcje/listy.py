moja_lista = list()
moja_lista = [1, 2, 3, 4, 5, 6, 'a']
print(dir(moja_lista))


# 'append', 'clear', 'copy', 'count', 'extend', 
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

moja_lista.append(10)
print(moja_lista)


x = [1, 2, 3]
y = x
y.append(5)
print(x, y)
print(id(x), id(y))

y = x[:]
y = x.copy()
y.append(5)
print(x, y)
print(id(x), id(y))


z = [1, 2]
x = [1, 2, z]

print(x) # [1, 2, [1, 2]]

import copy

y = copy.deepcopy(x)
print(y)

z.append(4)
print(x, y)
