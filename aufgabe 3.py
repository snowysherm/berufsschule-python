geldbetrag = float(input("Geldbetrag: "))
zinssatz = float(input("Zinssatz: "))
jahreszins = geldbetrag / 100 * zinssatz * 12
print(f"Jahreszins: {jahreszins}")
