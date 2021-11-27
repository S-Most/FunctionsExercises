# Oefenen met Parameters

# Functies zijn handig voor herhalende stukken code. Je kan de functies echter wel andere dingen laten doen aan de hand van de input.


def berekening(getal1, operatie, getal2):
    if operatie == "+":
        uitkomst = getal1 + getal2
    elif operatie == "-":
        uitkomst = getal1 - getal2
    print(uitkomst)


print("Functie 1:")
berekening(8, "-", 3)

try:
    print("De uitkomst is", uitkomst)
except NameError:
    print("Uitkomst is onbekend!")
    pass


def berekening2(getal1, operatie, getal2):
    if operatie == "+":
        uitkomst = getal1 + getal2
    elif operatie == "-":
        uitkomst = getal1 - getal2
    return uitkomst


antwoord = berekening2(8, "-", 3)
print("Functie 2:")
print("De uitkomst is", antwoord)
# Maak een functie die elk nth element uit de getallenreeks printen

# getallen = range(0,20)

# def nElement(reeks, n):
#     for i in range(n, len(reeks), n):
#         print(i)

# nElement(getallen, 3)
# nElement(getallen, 4)

# # Oefenen met returnwaardes

# # Soms wil je echter de uitkomst van een functie later in je script gebruiken. Je moet deze waarde dan "teruggeven" aan je script

# # Maak een functie die het element teruggeeft op de aangegeven plek keer 2

# def nElement2(reeks, n):
#     if 0 < n * 2 < len(reeks):
#         return reeks[n*2]
#     else:
#         return False

# nGetal3 = nElement2(getallen, 3)
# print(nGetal3)

# nGetal8 = nElement2(getallen, 8)
# print(nGetal8)
