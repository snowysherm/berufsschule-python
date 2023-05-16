grundstückslänge = float(input("Grundstückslänge: "))
grundstücksbreite = float(input("Grundstücksbreite: "))
maklerprovision = float(input("Maklerprovision in %: "))
umsatzsteuersatz = float(input("Umsatzsteuersatz in %: "))
quadratmeterpeis = float(input("Quadratmeterpreis: "))

grundstücksfläche = grundstückslänge * grundstücksbreite
nettopreis = grundstücksfläche * quadratmeterpeis
bruttopreis = nettopreis / umsatzsteuersatz + nettopreis
maklerprovision_geld = bruttopreis / maklerprovision

print(f"Bruttopreis in Euro: {bruttopreis}")
print(f"Maklerprovision in Euro: {maklerprovision_geld}")