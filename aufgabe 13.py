kandidat1 = input("Kandidat 1: ")
kandidat1_stimmen = float(input("Kandidat 1 stimmen: "))
kandidat2 = input("Kandidat 2: ")
kandidat2_stimmen = float(input("Kandidat 2 stimmen: "))
kandidat3 = input("Kandidat 3: ")
kandidat3_stimmen = float(input("Kandidat 3 stimmen: "))
kandidat4 = input("Kandidat 4: ")
kandidat4_stimmen = float(input("Kandidat 4 stimmen: "))

gesamt_stimmen = kandidat4_stimmen + kandidat3_stimmen + kandidat2_stimmen + kandidat1_stimmen
kandidat1_prozente = gesamt_stimmen / 100 * kandidat1_stimmen
kandidat2_prozente = gesamt_stimmen / 100 * kandidat2_stimmen
kandidat3_prozente = gesamt_stimmen / 100 * kandidat3_stimmen
kandidat4_prozente = gesamt_stimmen / 100 * kandidat4_stimmen

print(f"{kandidat1}: {kandidat1_prozente}%, {kandidat2}: {kandidat2_prozente}%, {kandidat3}: {kandidat3_prozente}%, {kandidat4}: {kandidat4_prozente}%")