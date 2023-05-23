print("1. Addition"
      "\n2. Subtraktion"
      "\n3. Multiplikation"
      "\n4. Division")

aufgabe = int(input("Wahl: "))

if aufgabe == 1:
    summand1 = int(input("Summand: "))
    summand2 = int(input("Summand: "))
    summe = summand1 + summand2
    print(f"{summand1} + {summand2} = {summe}")
elif aufgabe == 2:
    minuend = int(input("Minuend: "))
    subtrahend = int(input("Subtrahend: "))
    differenz = minuend - subtrahend
    print(f"{minuend} - {subtrahend} = {differenz} ")
elif aufgabe == 3:
    faktor1 = int(input("Faktor: "))
    faktor2 = int(input("Faktor: "))
    produkt = faktor1 * faktor2
    print(f"{faktor1} * {faktor2} = {produkt}")
elif aufgabe == 4:
    dividend = int(input("Dividend: "))
    divisor = int(input("Divisor: "))
    quotient = dividend / divisor
    print(f"{dividend} : {divisor} = {quotient}")
