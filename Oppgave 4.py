"""
1. Lag en FOR-loop som skriver ut alle tallene mellom 0 og 100
2. Foandre FOR-loopen slik at den kun skriver ut tall som er delig på 2
3. Lag en FOR-loop som leger sammen alle tallene fra 1-100
"""
# Del oppgave 1
for value in range(100):
    print(value)

# Del oppgave 2
for value in range(100):
    if value % 2 == 0:
        print(value)

# Del oppgave 3

total = 0
for value in range(100):
    total = total + value
print(total)