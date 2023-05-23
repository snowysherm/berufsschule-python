from random import randint

print("\n1. Addition"
      "\n2. Subtraktion"
      "\n3. Multiplikation"
      "\n4. Division")

aufgabe = int(input("Rechenart auswählen: "))
counter = int(0)

for i in range(1, 11):
    zahl1 = randint(1, 100)
    zahl2 = randint(1, 100)
    if aufgabe == 1:
        print(f"{zahl1} + {zahl2}")
        ergebnis = zahl1 + zahl2
    elif aufgabe == 2:
        print(f"{zahl1} - {zahl2}")
        ergebnis = zahl1 - zahl2
    elif aufgabe == 3:
        print(f"{zahl1} * {zahl2}")
        ergebnis = zahl1 * zahl2
    elif aufgabe == 4:
        print(f"{zahl1} : {zahl2}")
        ergebnis = zahl1 / zahl2
    u_input = int(input("Ergebnis: "))
    if u_input == ergebnis:
        counter += 1
        print("Richtig!")
    else:
        print("Falsch.")

print(f"Du hattest {counter} von 10 Aufgaben richtig.")