zahl = int(input("Zahl: "))
multiplikator = int(input("Multiplikator: "))
dings = int(1)
stop = int(1)

while stop < multiplikator + 1:
    ergebnis = zahl * dings
    print(ergebnis)
    dings += 1
    stop += 1
