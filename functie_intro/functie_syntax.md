# Omschrijving
Wat zijn de mogelijkheden met functies, hoe maak je een functie en hoe gebruik je deze?
Dit leggen we uit aan de hand van een kookboek.

```python
def doe_iets(parameters):
    """Uitleg over wat de functie doet"""*

    ...jouw code...
    return iets*
```
_lines aangegeven met * zijn optioneel_


## Recept voor een functie

1. `def` geeft aan dat je een functie gaat definiëren.
2. `functie`: je geeft de functie een naam, deze beschrijft wat de functie doet. In ons voorbeeld heet de functie `doe_iets`.
3. `parameters`: Je mag zoveel parameters meegeven als je wil en ze kunnen van alle verschillende typen zijn. Deze kan je dan in functie gebruiken.
3. De functie declaratie eindigt altijd met een dubbele punt, net zoals bij if-statements en for-loops.
4. Mocht de naam van je functie niet beschrijvend genoeg zijn, dan kan je met commentaar de functie nog verder beschrijven.
5. Één of meerdere python statements komen in de functie te staan.
6. `return iets`: Je waarde(n) van een functie retourneren, zoals bijvoorbeeld de uitkomst van een berekening. Zodra de interpreter een `return` tegenkomt, wordt een waarde geretourneerd en ga je direct uit de functie.


## Een functie gebruiken
Een functie kan je aanroepen door buiten je functie-declaratie de functie te noemen (met evt parameters).

### Voorbeeld
Deze functie groet een persoon naar wens.

```python
def groet(naam): # hier declareren we de functie
    print(f"Hallo {naam}!")

groet("Jan") # hier roepen we de functie aan
```
Output
```bash
> Hallo Jan!
```


# volgende pagina functie output/returns
