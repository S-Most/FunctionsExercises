# Omschrijving
Heb je vaak het idee dat je programma op een makkelijker manier geschreven kan worden?
Python heeft dan voor jou de perfecte oplossing, functies.

```info
Een functie in python is een groepje nauwverwante code dat een specifieke taak uitvoert.
```

Stel je maakt een programma dat checkt of een woord een `even` of een `oneven` aantal karakters bevat:
```python
woord = "bit"
if len(woord) % 2 == 0: # de lengte van het woord is even
    print("even")
else 
    print("oneven")
```
Output
```bash
> oneven
```

Voor deze case werkt bovenstaande code prima.
Maar wat als je nu later in je programma precies hetzelfde wil checken?

```python
woord = "bit"
if len(woord) % 2 == 0: # de lengte van het woord is even
    print("even")
else 
    print("oneven")

... # overige code

ander_woord = "-academy"
if len(ander_woord) % 2 == 0:
    print("even")
else
    print("oneven")
```
Output
```bash
> oneven
> even
```

Nu merk je dat je twee keer hetzelfde aan het schrijven bent. Dat kan beter. Nu hetzelfde programma, maar dan met gebruik van een functie:
```python
def checkEvenOfOneven(woord):
    if len(woord) % 2 == 0: # de lengte van het woord is even
        print("even")
    else 
        print("oneven")

woord = "bit"
checkEvenOfOneven(woord)

... # overige code

ander_woord = "academy"
checkEvenOfOneven(ander_woord)
```
Output
```bash
> oneven
> even
```

Probeer eens zelf een functie te maken in `Python`.

```exercise
Maak een functie die checkt of 'a' in een string zit. Als 'a' in de string zit, print "a zit in de string", anders "a zit niet in de string"
```

# Volgende pagina -> functie syntax
