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
2. `functie`: je geeft de functie een naam, deze beschrijft wat de functie doet. In ons voorbeeld heet de functie `doe_iets`.
3. `parameters`: Je mag zoveel parameters meegeven als je wil en ze kunnen van alle verschillende typen zijn. Deze kan je dan in de functie gebruiken.
3. De functie header eindigt altijd met een dubbele punt, net zoals bij if-statements en for-loops.
4. Mocht de naam van je functie niet beschrijvend genoeg zijn, dan kan je met commentaar de functie nog verder beschrijven.
5. Één of meerdere python statements komen in de functie te staan.
6. `return iets`: Je mag waarde(n) van een functie retourneren, zoals bijvoorbeeld de uitkomst van een berekening. Zodra de interpreter een `return` tegenkomt, wordt een waarde geretourneerd en ga je direct uit de functie.


## Een functie gebruiken
Een functie kan je aanroepen door buiten je functie-declaratie de functie te aan te roepen (met evt parameters).

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


> volgende blok -> functie input en output
