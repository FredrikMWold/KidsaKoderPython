"""
1. Lag et program som lagrer en input i en variabel og skriv den ut igjen.
2. Lag en liten kalkulator som tar 2 tall som input, legger dem sammen og skriver ut svaret.
3. Lag et program som tar navnet og alderen din som input og skriver ut en hilsen.
"""

var = input("Skriv inn noe: ")
print(var)

tall1 = int(input("Skriv in et tall: "))
tall2 = int(input("Skriv in et tall: "))
print(tall1 + tall2)

navn = input("Hva er navnet ditt: ")
alder = int(input("Hvor gammel er du: "))
print("Jeg heter " + navn + " og er " + alder + " år gammel ")