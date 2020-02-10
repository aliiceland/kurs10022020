"""
Napisz program, ktory wypisze tabliczkę mnożenia NxN

Np N=3

    0 1 2 3

0   0 0 0 0
1   0 1 2 3
2   0 2 4 6
3   0 3 6 9 

"""

N = 10

print("     ", end="")

for i in range(N+1):
    print(f"{i:4}", end="")

print()
print()

for i in range(N+1):
    print(f'{i:<5}', end="")
    for j in range(N+1):
        print(f"{i*j:4}", end="")
    print()