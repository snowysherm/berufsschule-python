# def berechne_mehrwertsteuer(preis):
#     mehrwertsteuer = preis * 0.19
#     return mehrwertsteuer
#
#
# def main():
#     preis = float(input("Preis eingeben: "))
#     mehrwertsteuer = berechne_mehrwertsteuer(preis)
#     gesamtpreis = preis + mehrwertsteuer
#     print("Mehrwertsteuerbetrag:", mehrwertsteuer)
#     print("gesamt:", gesamtpreis)
#
#
# main()

preis = float(input("Preis:"))
mehrwertsteuer = preis * 0.19
gesamtpreis = preis + mehrwertsteuer
print(gesamtpreis)