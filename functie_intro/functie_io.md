# Omschrijving
Een functie kan verschillende inputs en outputs hebben.

![](function.jpg)

De parameters zijn de inputs van een functie.
Wat je returnt is de output van een functie.
Zowel de parameters als de return zijn optioneel.


### Voorbeeld
Stel je hebt een functie die de oppervlakte en de omtrek van een cirkel bepaalt, aan de hand van de diameter van de cirkel. \
`inputs`: diameter van een cirkel \
`outputs`: oppervlakte en omtrek

```python

def opp_en_omtrek(diameter):
    """Bereken de oppervlakte en omtrek, aan de hand van een diameter van een cirkel"""
    straal = diameter / 2
    opp = 3.14 * (straal ** 2)
    omtr = 2 * 3.14 * straal

    return opp, omtr

oppervlakte, omtrek = opp_en_omtrek(10)
print(f'Oppervlakte = {oppervlakte} en Omtrek = {omtrek}')
```

Output
```bash
> Oppervlakte = 314 en Omtrek = 62.8
```


```exercise
Maak een functie die volume van een kubus berekent. Alle zijden van een kubus zijn even lang. Bereken vervolgens de volumes van kubussen van lengtes 5, 10 en 20.
```
