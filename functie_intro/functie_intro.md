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

Nu merk je dat je twee keer hetzelfde aan het schrijven bent. Nu hetzelfde programma, maar dan met gebruik van functies:
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

# Volgende pagina -> functie syntax
