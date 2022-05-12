
# Voorbereidingen voor een test
Voordat de test gemaakt kan worden door de kandidaten moet je de volgende dingen doen. **Deze stappen moeten op alle laptops worden 
uitgevoerd!**

1. Zorg ervoor dat op elke pc waar de test gemaakt gaat worden het bestand ```quiz_afleveringnummer.txt```
in de map ``test_files`` staat.
   
2. Het bestand ``joker_vrijstellingen.txt`` moet bijgewerkt zijn. Dit houdt in dat achter de mol een ``x``
moet komen te staan. Achter elke speler die een vrijstelling heeft gebruikt moet ook een ``x`` komen te staan. 
   Achter elke speler die een of meer jokers heeft gebruikt moet het aantal jokers achter de naam 
   van die persoon gezet worden. In het geval dat er een zwarte vrijstelling is gebruikt moet er alleen een 
   ``x`` komen achter de mol, de jokers worden in dit geval ook niet genoteerd.
   

# Voorbereidingen executie
Deze stappen moeten uitgevoerd worden op alle laptops waar de executie niet op gedaan wordt,
zeer waarschijnlijk jouw laptop.

1. Open de map losse_csv en kopieer het bestand ``quiz_afleveringnummer_username.csv`` naar de usb-stick. ``username``
   is een identificator waaraan je kan zien van welke laptop de csv afkomt. Dit is nodig zodat alle bestanden een unieke 
   naam hebben zodra ze op jouw laptop staan. 
2. Herhaal stap 1 op alle laptops behalve de jouwe.
3. Stop de usb-stick nu in jouw laptop en stop alle ``quiz_afleveringnummer_username.csv`` bestanden in de map
```losse_csv``` op jouw computer.
   
4. Open het bestand ``loginnamen.txt``. Hierin moet je alle verschillende ``username`` die aan het
eind van de bestanden ``quiz_afleveringnummer_username.csv`` staan. In andere woorden, alle gebruikersnamen
   van alle laptops waarop de test gemaakt is moeten hierin staan, ook de gebruikers naam van jouw laptop moet hierbij staan.
   Er mogen hier niet te veel gebruikers namen instaan. Dus stel test ``1`` is gemaakt op de laptop met username ``barta``
   maar test ``2`` niet meer, dan moet ``barta`` uit het bestand gehaald worden. Elke gebruikersnaam moet op een eigen regel staan
   net als bij de vragen en antwoorden text files.
   


# Errors executie
In de map ``executie_logs`` kan je alle log bestanden vinden van de executies, ze zijn genummerd op afleveringnummer.
In een log bestand kan je precies zien wat het programma heeft uitgevoerd en of er een error is geweest.
Elke regel geeft informatie over een onderdeel van het programma. Het volgende format wordt gehanteerd: datum - info/error - bericht.
``Info/error`` geeft aan of het er een error heeft plaatsgevonden, de ``info`` tag betekent dat ìets goed verlopen is. Zodra er
error staat betekent dit dat er iets niet goed verlopen is. Zodra dit het geval is kan je het bericht kopiëren en opzoeken
in deze readme. Deze readme geeft dan precies aan welke stappen je moet ondernemen om de error op te lossen.

## Het bestand van ``inlognaam`` ontbreekt in de map losse_csv
Dit kan twee dingen betekenen:
1. Het inlognamen bestand klopt niet. Dit betekent dat hier een laptop naam in staat die niet gebruikt is voor de huidige
test. Dit los je op door in het bestand inlognamen onder elkaar alleen de namen te zetten van de laptops waarop
   de huidige test gemaakt is.
   
2. Het bestand van de laptop met de ``inlognaam`` ontbreekt in de map ``losse_csv``. Dit is op te lossen door het bestand
van de laptop van ``inlognaam`` op de usb-stick te zetten en vervolgens op jouw laptop te zetten.
   
## De volgende mensen hebben twee keer de test gemaakt:
Dit betekent dat de mensen die geprint worden de test twee keer gemaakt hebben. Dit kan je oplossen
door naar de map ``losse_csv`` te gaan en in alle csv bestanden van dat quiz nummer te kijken waar die persoon dubbel in staat.
Vervolgens verwijder je een van die regels uit het bestand en dat heeft diegene de test maar 1 keer gemaakt.

## ``persoon`` zit in het spel maar heeft de test nog niet gemaakt
Dit kan twee redenen hebben:
1. De persoon moet de test nog maken. Dit kan je doen door de test opnieuw te openen op jouw laptop en die persoon hem
nog laten maken op jouw laptop.
   
2. Het bestand ``jokers_vrijstellingen`` klopt niet. Je kan dit oplossen door de persoon die uit het spel ligt en die toch aangegeven
wordt als in het spel uit het bestand ``jokers_vrijstellingen.txt`` te halen.
   
# De volgende mensen hebben de test gemaakt terwijl ze uit het spel liggen:
Dit kan drie redenen hebben:
1. Iemand heeft de test gemaakt maar die persoon ligt uit het spel. Dit kan je oplossen door naar de csv van de bijbehorende test te gaan in de map
``losst_csv`` en de regel van die persoon uit de csv te halen. Nu kan je de executie code opnieuw uitvoeren.
   
2. Het ``jokers_vrijstellingen.txt`` bestand klopt niet. Deze kan je openen en de naam van de persoon erbij typen.

3. Iemand heeft zijn naam verkeerd getypt. Dit kan je oplossen door naar de csv in het mapje ``losse_csv`` te gaan en daar de
verkeerd getypte naam te veranderen zodat die goed gespeld is. 
   




## Het lettertype is niet hetzelfde als op tv.
Dit betekent dat de font niet is geinstalleerd op de laptop. Doe dit door het bestand ``OCRAEXT.TTF`` te openen
en op installeren te drukken. 

## 