from random import randint

counter = int(0)

for i in range(1, 11):
    zahl1 = randint(1, 100)
    zahl2 = randint(1, 100)
    print(f"{zahl1} + {zahl2}")
    u_input = int(input("Ergebnis: "))
    ergebnis = zahl1 + zahl2
    if u_input == ergebnis:
        counter += 1
        print("Richtig!")
    else:
        print("Falsch.")

print(f"Du hattest {counter} von 10 Aufgaben richtig.")

