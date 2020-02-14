import random
"""
Lag et spill hvor programmet ditt velger et tilfeldig tall. Spilleren skal prøve å gjette hva dette tallet er.
Hvis spilleren gjetter feil skal programmet fortelle spillerne om de gjettet for høyt eller for lavt.
Spilleren må da gjette på ny helt til de finner riktig tall.
"""

hemmligTall = random.randint(0,100)

while True:
    gjett = int(input("Skriv inn et tall: "))
    if gjett == hemmligTall:
        print("Du gjettet rikrig")
        break
    elif gjett < hemmligTall:
        print("Tallet er høyere")
    elif gjett > hemmligTall:
        print("Tallet er lavere")