x, y =  101, 200

if x > 100 or y > 100 or x < 0 or y < 0:
    print("Poza planszą")
elif x =< 10 and y >= 90:
    print("LG")
elif x >= 90 and y >= 90:
    print("PG")
elif x >= 90 and y <= 10:
    print("PD")
elif x <= 10 and y <= 10:
    print("LD")
elif x >= 90:
    print("PK")
elif x <= 10:
    print("LK")
elif y >= 90:
    print("GK")
elif y <= 10:
    print("DK")
else:
    print("Centrym")