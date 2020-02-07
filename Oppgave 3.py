"""
1. Lag en IF-statement som sammenligner to tall.
2. Lag en IF-statement som sammneligner to strings.
3. Lag et program som tar to inputs, et brukernavn og et passord. Sjekk deretter om brukernavn og passord er riktig, og skriv ut en velkomst melding hvis det stemmer.
   Skriv ut en varsel melding hvis det er feil.
"""

# Del oppgave 1

tall1 = 6
tall2 = 6

if tall1 == tall2:
    print("Rkitig")
else:
    print("Ikke riktig")

# Del oppgave 2

tekst1 = "Hey"
tekst2 = "hey"

if tekst1 == tekst2:
    print("riktig")
else:
    print("Hey er ikke det samme som hey")

# Del oppgave 3

brukernavn = input("Skriv inn ditt brukernavn: ")
passord = input("Skriv inn ditt passord")

if brukernavn == "Fredrik" and passord == "Hemmelig":
    print("Velkomen")
else:
    print("Feil brukernavn eller passord")