# Omschrijving
## Hoe maak je een functie en hoe gebruik je deze? 
Eerst schrijf je de definitie van je functie. Hiereen geef je aan wat je functie doet.

```python
def doe_iets(parameters):
    """Uitleg over wat de functie doet""" *

    ...jouw code...
    return iets *
```
_lines aangegeven met * zijn optioneel_


## Functie syntax

1. `def` geeft aan dat je een functie gaat definiëren.
1. `functie`: je geeft de functie een naam, deze beschrijft wat de functie doet. In ons voorbeeld heet de functie `doe_iets`.
1. `parameters`: Je mag zoveel parameters meegeven als je wil en ze kunnen van alle verschillende typen zijn. Deze kan je dan in de functie gebruiken.
3. De functie header eindigt altijd met een dubbele punt, net zoals bij if-statements en for-loops.
4. Mocht de naam van je functie niet beschrijvend genoeg zijn, dan kan je met commentaar de functie nog verder beschrijven.
5. Één of meerdere python statements komen in de functie te staan.
6. `return iets`: Je mag waarde(n) van een functie retourneren, zoals bijvoorbeeld de uitkomst van een berekening. Zodra de interpreter een `return` tegenkomt, wordt een waarde geretourneerd en ga je direct uit de functie.

```info
Een parameter is een 'input' van een functie. Een parameter kan van elk type zijn. Een parameter wordt een lokale variabele binnen de functie. Zodra je uit de functie gaat, bestaat deze variabele niet meer. *Wil je een functie variabele buiten de functie weer gebruiken, gebruik dan een `return`.*
```

## Een functie gebruiken
Een functie kan je aanroepen door buiten je functie-declaratie de functie aan te roepen (met evt parameters).

### Voorbeeld
Deze functie groet een persoon naar wens.

```python
def groet(naam): # hier declareren we de functie
    print(f"Hallo {naam}!")

groet("Jan") # hier roepen we de functie aan
groet("Anna") # we kunnen de functie zo vaak aanroepen als we willen
```
Output
```bash
> Hallo Jan!
> Hallo Anna!
```


Maak een functie die gegeven een lijst met namen(strings), alle personen uit die lijst groet, gebruikmakend van de bovenstaande `groet` functie.
Gebruik deze lijst:
```python
namen = ["Jan", "Anna", "Gijs", "Brechtje", "Bert", "Bob"]
```
##  Nieuwe technieken
NVT

## Herhaalde technieken
Functies

## Verwachte uitkomst
```bash
> Hallo Jan!
> Hallo Anna!
> Hallo Gijs!
> Hallo Brechtje!
> Hallo Bert!
> Hallo Bob!
```

## Nakijkcriteria
- Er wordt gebruikgemaakt van de `groet` functie
- Alle personen worden gegroet
- Er worden twee functies in totaal gedeclareerd.

> volgende blok -> functie input en output
