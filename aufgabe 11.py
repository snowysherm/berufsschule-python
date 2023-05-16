körpergröße = float(input("Körpergröße in m: "))
körpergewicht = float(input("Körpergewicht: "))
geschlecht = input("Geschlecht m/w: ")

bmi = körpergewicht / (körpergröße ** (2))

if (geschlecht == 'm' and bmi < 20):
    print(f"UNTERGEWICHT XD, bmi: {bmi}")
elif (geschlecht == 'm' and bmi > 25):
    print(f"übergewicht :(, bmi: {bmi}")
elif (geschlecht == 'm' and 20 <= bmi <= 25):
    print(f"normal, bmi: {bmi}")
elif (geschlecht == 'w' and bmi < 19):
    print(f"untergewicht, bmi: {bmi}")
elif (geschlecht == 'w' and bmi > 24):
    print(f"übergewicht, bmi: {bmi}")
elif (geschlecht == 'w' and 29 <= bmi <= 24):
    print(f"normal, bmi: {bmi}")
