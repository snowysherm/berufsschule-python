preis = float(input("Preis:"))
gezahlt = float(input("Gezahlt:"))

if (gezahlt < preis):
    print("zu wenig gezahlt")
else:
    print(f"Rückgeld: {gezahlt - preis}")