a = float(input("Seitenlänge a:"))
b = float(input("Seitenlänge b:"))
c = float(input("Seitenlänge c:"))

volumen = a*b*c
oberflaeche = 2*a*b+2*a*c+2*b*c
raumdiagonale = a**(2)+b**(2)+c**(2)**(0.5)

print(f"Volumen: {volumen}, Oberflaufäche: {oberflaeche}, Raumdiagonale: {round(raumdiagonale, 2)}")