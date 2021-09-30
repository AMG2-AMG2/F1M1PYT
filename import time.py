import time

vraag1 = 'Wat doe jij in de ochtend'
a1 = 'a = Telefoon bekijken'
b1 = 'b = Ontbijten'
c1 = 'c = Douche' 

vraag2 = 'Wat doe je als je weg gaat van huis?'
a2 = 'a = Niks'
b2 = 'b = Naar school'
c2 = 'c = Naar werk' 

vraag3 = 'Met wat ga je naar je werk of school?'
a3 = 'a = OV'
b3 = 'b = Auto'
c3 = 'c = Scooter' 

vraag4 = 'Wat doe je als je weer thuis kom'
a4 = 'a = film kijken'
b4 = 'b = Met vrienden afspreken'
c4 = 'c = Gamen' 

vraag5 = 'Wat doe jij in de avond'
a5 = 'a = slapen'
b5 = 'b = Youtube kijken en te laat slapen'
c5 = 'c = feesten' 

print(vraag1)
time.sleep(1)
print(a1)
time.sleep(1)
print(b1)
time.sleep(1)
print(c1)
time.sleep(1)
antwoord1 = input()
if antwoord1 == 'a':
    print("Ik doe dat ook altijd!")
elif antwoord1 == 'b':
    print("lekker eten!!")
else:
    print(antwoord1, "dat doe ik nooit")

time.sleep(1)
print(vraag2)
time.sleep(1)
print(a2)
time.sleep(1)
print(b2)
time.sleep(1)
print(c2)
time.sleep(1)
antwoord2 = input()
if antwoord2 == 'a':
    print("Ik doe dat niet!")
elif antwoord2 == 'b':
    print("Ik doe dat 5 keer per week")
else:
    print(antwoord2, "Ik doe dat nog niet")
time.sleep(1)

time.sleep(1)
print(vraag3)
time.sleep(1)
print(a3)
time.sleep(1)
print(b3)
time.sleep(1)
print(c3)
time.sleep(1)
antwoord3 = input()
if antwoord3 == 'a':
    print("Ik doe dat bijna nooit meer.")
elif antwoord3 == 'b':
    print("Ik doe dat soms")
else:
    print(antwoord3, "Ik doe dat bijna elke dag")
time.sleep(1)

time.sleep(1)
print(vraag4)
time.sleep(1)
print(a4)
time.sleep(1)
print(b4)
time.sleep(1)
print(c4)
time.sleep(1)
antwoord4 = input()
if antwoord4 == 'a':
    print("Ik doe dat in de avond.")
elif antwoord4 == 'b':
    print("Ik doe dat soms")
else:
    print(antwoord4, "Ik doe dat bijna elke dag")
time.sleep(1)

time.sleep(1)
print(vraag5)
time.sleep(1)
print(a5)
time.sleep(1)
print(b5)
time.sleep(1)
print(c5)
time.sleep(1)
antwoord5 = input()
if antwoord5 == 'a':
    print("Niet echt.")
elif antwoord5== 'b':
    print("Ik doe dat soms")
else:
    print(antwoord5, "Ik doe dat bijna elke dag")
time.sleep(1)