## 🟦Beskrivning
Projektet "06_oop" innehåller lösningen av veckouppgift 6 under 
YH-kursen Testautomation med Python vid NBI Handelsakademin.  
Uppgiften omfattar 4 programmeringsuppgifter som redovisas på GitHub.

## Innehåll
1. Läsa och förstå kod
2. Länder
3. Banken
4. Webbshop

### 1️⃣ Läsa och förstå kod
Uppgiften innebar att ett antal oop kodexempel skulle tolkas. I första uppgiften
skulle en förväntad utskrift gissas. Den andra uppgiften var ett exempel med en 
basklass och två klasser som ärvde denna. I uppgiftens lösande ingick att tolka
vad koden gjorde och att rätta några fel i koden. Slutligen skulle man lägga till
en egen klass som ärvde samma basklass.

### 2️⃣ Länder
I uppgiften ingick en klass som (Country) som instansierade objekt med variablerna 
"name" och "population".  
1. Skapa objekt för länderna. (Data från januari 2024. Avrunda befolkningen.)  
2. Lägg till en metod med namnet "print_info". Om man anropar den för Sverige-objektet 
ska den skriva ut: "I Sverige bor det 10.5 miljoner invånare". Metoder ska använda klassens 
egenskaper, så att den fungerar för de andra länderna och inte bara för Sverige.
3. Lägg till landets area som en egenskap till klassen. Använd en parameter till konstruktorn, 
alltså __init__ metoden. Ge arean ett default värde på None så att man inte måste ange arean 
när man skapar ett landsobjekt.
4.  Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.
5. Skapa en ny metod med namnet "add_language". Den ska lägga till ett av landets officiella språk. 
(Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.) 
För att kunna spara ett varierande antal behöver du använda en lista.
6. Ändra i "print_info" så att den skriver ut alla officiella språk, på en ny rad.

### 3️⃣Banken
Skapa en klass som representerar ett bankkonto. Banken ska kunna:
1. sätta in pengar (deposit)
2. ta ut pengar (withdraw)
3. returnera nuvarande saldo (balance)
4. räkna ut ränta (apply_interest, lägger till räntan till kontot)
5. tala om ifall man har råd att betala en räkning (returnera True/False)
6. Gör en metod för varje funktionalitet. 
7. Skriv enhetstester för varje funktion. Använd gärna TDD-metoden, 
att börja med testfallen innan du skriver koden.

### 4️⃣ Webbshop
Skapa klasser som representerar en webbshop:
- produkter (Product)
- beställningar (Order)
- kundvagn (ShoppingCart)

Klassen WebShop utgör kontrollklass för programmet och klassen äger produktlista, 
kundvagn och lista med lagda order. Klassen Product skapar produktobjekt och används 
av WebShop för att skapa en produktförteckning. Listan med produkter styrs från 
WebShop varifrån man kan visa listan och hämta enskilda objekt. Klassen ShoppingCart
används av webshop för att skapa en varubeställning. Användaren kan lägga till och 
ta bort objekt från varukorgen samt visa nuvarande summa för objekten i varukorgen. 
Klassen kan även tömma varukorgen och presentera den på ett snyggt sätt. Då en beställning 
läggs skapar klassen Orders en kopia av innehållet i kundvagnen och sparar denna som en
sluförd order.


   
## 📊 Status

Här nedan presenteras en översikt över statusen på lösande av uppgfterna.

| Uppgift                | Status |
|:-----------------------|:------:|
| 1. Läsa och förstå kod |   🟢   |
| 2. Länder              |   🟢   |
| 3. Banken              |   🟢   |
| 4. Webbshop            |   🟢   |
