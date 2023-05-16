from random import randint

zahl1 = randint(1,100)
zahl2 = randint(1,100)

zahl3 = zahl1 + zahl2

print(f"Zahl 1: {zahl1}, Zahl 2: {zahl2}")
ergebnis_user = float(input("Bitte addieren und Ergebnis eingeben!: "))

if (zahl3 == ergebnis_user):
    print("Richtig! YIPPIE")
else:
    print("Nicht richtig! :(")