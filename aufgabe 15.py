literpreis = float(input("Literpreis Benzin: "))
verbrauchte_liter = float(input("Verbrauchte Liter: "))
gefahrene_km = float(input("Gefahrene Kilometer: "))

# Ausgabe: Verbrauch pro 100 km, Preis pro 100 km, Preis Gesamtstrecke

verbrauch_100km = verbrauchte_liter / gefahrene_km * 100
preis_100km = literpreis * verbrauch_100km
preis_gesamt = verbrauchte_liter * literpreis

print(f"Verbrauch pro 100 km: {verbrauch_100km}")
print(f"Preis pro 100 km: {preis_100km}")
print(f"Gesamtpreis: {preis_gesamt}")