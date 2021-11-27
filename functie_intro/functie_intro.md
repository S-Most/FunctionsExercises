# Omschrijving
Heb je vaak het idee dat je code op een handiger manier geschreven kan worden? Python heeft dan voor jou de perfecte oplossing, functies.


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
def even_of_oneven(woord): # hier declareren we de functie
    if len(woord) % 2 == 0: 
        print("even")
    else 
        print("oneven")

woord = "bit"
even_of_oneven(woord) # hier wordt de functie aangeroepen

ander_woord = "academy"
even_of_oneven(ander_woord)
```
Output
```bash
> oneven
> even
```

```info
Een functie is een groepje nauwverwante code dat een specifieke taak uitvoert.
```

```info
Functies zorgen ervoor dat je niet dezelfde code meerdere keren hoeft te schrijven.```


Probeer eens zelf een functie te maken in `Python`.

```exercise
Maak een functie die checkt of 'a' in de meegegeven variabele zit. Als 'a' in de variabele zit, print "a zit in {variabele}", anders "a zit niet in {variabele}".
Roep vervolgens deze functie meerdere keren aan met de volgende strings: "functies", "zijn", "handig".
```

## Verwachte uitkomst
```bash
> a zit niet in functies
> a zit niet in zijn
> a zit in handig
```

> Volgende blok -> functie syntax
