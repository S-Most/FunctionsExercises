# Python Novice -> Back to Basics extra uitleg en exercises over functies
Python Novice->2.Back to basics -> 5. Rekenmachine is de enige exercise die over functies in het Data traject.
Aangezien functies een vrij fundamenteel onderwerp zijn in programmeren, lijkt het me goed om wat meer aandacht eraan te bestedem.
Daarom heb ik drie exercises gemaakt om de student meer kennis te laten maken met functies.


# Exercise Functies Introductie
# Omschrijving
Heb je vaak het idee dat je code op een handiger manier geschreven kan worden? Python heeft dan voor jou de perfecte oplossing, functies.


Stel je maakt een programma dat checkt of een woord een **even** of een **oneven** aantal karakters bevat:
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

Nu merk je dat je twee keer hetzelfde aan het schrijven bent. Dat kan beter. Nu hetzelfde programma, maar dan met gebruik van een **functie**:
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
Een functie is een groepje nauwverwante code dat een specifieke taak uitvoert. [Documentatie](https://www.programiz.com/python-programming/function)
```

```info
Functies zorgen ervoor dat je niet dezelfde code meerdere keren hoeft te schrijven.
```


Maak een functie die checkt of karakter `a` in een string zit: 
- Als `a` in de string zit, print "a zit in {string}"
  - in alle andere gevallen: "a zit niet in {string}". 
  
`{string}` is de string waarin wordt gecheckt of `a` erin zit.
- Roep vervolgens deze functie meerdere keren aan met de volgende strings: `functies`, `zijn` en `handig`.

## Nieuwe technieken
Functies

## Verboden technieken
Meer dan 1 if-statement schrijven

## Verwachte uitkomst
```bash
> a zit niet in functies
> a zit niet in zijn
> a zit in handig
```

## Nakijkcriteria
1. Er is een functie gedefinieerd
2. Deze functie wordt meerdere keren aangeroepen met de strings van de opdracht

> Volgende blok -> functie syntax


# Documentatie gedachteproces

## Wat willen we bereiken?
De student begrijpt:
1. Wat een functie is
2. Wanneer functies nuttig zijn om te gebruiken

