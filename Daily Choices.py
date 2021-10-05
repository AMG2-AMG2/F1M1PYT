import time

vraag1 = 'Wat doe je als eerst in de ochtent'
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
c3 = 'c = Fiets' 

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
    print("Hmmmmmm klinkt lekker")
else:
    print(antwoord1, "dat doe ik nooit")
time.sleep(1)
