We hebben al best veel code uit de standaardbibliotheek gebruikt, denk aan `explode`, `is_numeric`  en `readline`. Dit zijn allemaal voorbeelden van ingebouwde functies in PHP. Super handig! Het voordeel van deze functies is dat we bepaald gedrag niet elke keer opnieuw hoeven op te schrijven, maar gewoon de functie kunnen aanroepen, die het gedrag voor ons uitvoert.

PHP bevat echter maar een beperkte hoeveelheid van deze functies. Als je grotere en complexere programma's schrijft, krijg je altijd gedrag wat op meerdere locaties in je applicatie nodig is. Bijvoorbeeld het maken van een verbinding met de database, het controleren of de huidige gebruiker iets mag doen of een gebruiker zijn credits bijwerken.

Zelf willen we dus ook code schrijven die we vervolgens op verschillende plekken kunnen gebruiken, net zoals `intval` of `readline`. En dat kan! In PHP heet dit een functie en functies kan je zelf maken!

Dat ziet er ongeveer zo uit:

```php
function foo() {
   echo "Here's the foo.";
}

foo();
```
Output
```bash
> Here's the foo.
```

```info
foo is een naam die vaak wordt gebruikt als voorbeeld naam voor functies.

Een ander voorbeeld hiervan wat je veel gebruikt ziet worden is 'bar'.
```

In de bovenstaande code gebeurt er een aantal dingen:

1. We gebruiken het woord `function` om aan te geven dat we een functie willen maken. 
2. We geven de functie de naam `foo`. 
3. De `()` hebben een speciale betekenis maar hier komen we straks op terug.
4. De accolades geven, net zoals bij een `if` statement, aan wat er binnen de functie hoort en wat niet.
5. Binnen de accolades, dus binnen de functie, roepen we `echo` aan.
6. Als laatste roepen we onze functie aan met `foo();`. Dat lijkt in gebruik heel erg veel op hoe bijvoorbeeld `intval` werkt.

Maar, dit voorbeeld was nog niet heel nuttig. Om dit te doen, kunnen we net zo goed gelijk `echo` aanroepen. Dus laten we naar een voorbeeld kijken waar een functie wél nuttig is.

Stel je wilt een bepaalde berekening met verschillende getallen kunnen doen.

```php
function complexMath($x) {
    echo $x * 10;
    echo PHP_EOL;
}

complexMath(100);
complexMath(10);
```

Zoals je kan zien doen we binnen de `complexMath` functie *hele* moeilijke berekeningen, maar er is ook iets anders toegevoegd: tussen de `()` staat nu een variable `$x`. Dit is een 'argument'. Met argumenten kunnen we het gedrag van een functie aanpassen. De `$x` moeten we nu elke keer als we `complexMath` aanroepen meegeven. Net als dat we aan `readline` mee konden geven wat voor een vraag er aan de gebruiker gesteld moest worden, kunnen we nu ook bepalen welk getal we meegeven!

```info
$x maken we nooit expliciet aan. We zeggen nergens $x = 10. $x bestaat namelijk alleen binnen onze functie en heeft geen leven daarbuiten. Dit noemen we de 'scope' van $x. Op 'scopes' komen we later terug! Voorlopig is het genoeg om te weten dat de $x variabele alleen binnen onze functie beschikbaar is.
```

Maar, wat nou als je een behoefte hebt die meer lijkt op `intval`. Weet je nog? Dit was dat je een variable meegeeft en `intval` kijkt of het iets is waar hij een getal van kan maken en daarna teruggeeft. Nou, dat proces vervullen kunnen wij zelf ook! Om een waarde terug te geven uit een functie gebruiken we het 'return' keyword. Kijk maar eens naar onderstaand voorbeeld.

```php
function complexMath($x) {
    return $x * 10;
}

echo complexMath(100) . PHP_EOL;
echo complexMath(10) . PHP_EOL;
```


Dit was een kort overzicht van de mogelijkheden van functie, het wordt pas echt interessant wanneer je zelf functies gaat schrijven met meer gedrag erin. Dus dat gaan we in de volgende exercises doen!