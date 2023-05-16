geldbetrag = float(input("Geldbetrag:"))
rabatt = float(input("Rabatt:"))
rabatt2 = geldbetrag / rabatt
betrag_nach_abzug = geldbetrag - rabatt2

if (rabatt > 100):
    print("Der Rabatt kann nicht über 100% sein")
else:
    print("Nach Abzug:", betrag_nach_abzug)