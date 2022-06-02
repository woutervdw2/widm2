# Het maken van een test tekst bestand
Het is hetzelfde als vorig jaar. In de map ``test_files`` kan je txt bestanden zetten.
Stel je wilt alle vragen erin zetten voor aflevering 4, dan noem je het ``quiz_4.txt``. Elke vraag moet eindigen met een
vraagteken. In de regels die daarop volgen plaats je de antwoorden. Voor het goede antwoord plaats je een ``!``. 
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
   
3. Open windows verkenner en ga naar de map van het programma.
4. Type in de zoekbalk ``cmd`` en druk op enter.
5. Type in cmd ``py open_txt.py`` in en druk op enter. De test wordt nu gestart.
6. Type in het eerste venster het test nummer en klink op de enter knop. Laat nu iedereen een voor een de test maken.
7. Zodra iedereen de test gemaakt heeft kun je cmd afsluiten, dit zal ook het test venster sluiten.

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
eind van de bestanden ``quiz_afleveringnummer_username.csv`` staan zetten. In andere woorden, alle gebruikersnamen
   van alle laptops waarop de test gemaakt is moeten hierin staan, ook de gebruikers naam van jouw laptop moet hierbij staan.
   Er mogen hier niet te veel gebruikers namen instaan. Dus stel test ``1`` is gemaakt op de laptop met username ``barta``
   maar test ``2`` niet meer, dan moet ``barta`` uit het bestand gehaald worden. Elke gebruikersnaam moet op een eigen regel staan
   net als bij de vragen en antwoorden text files.
   
5. Open windows verkenner en ga naar de map van het programma.

6. Type in de zoekbalk ``cmd`` en druk op enter.

7. Type in cmd ``py executie.py`` in en druk op enter. De executie wordt nu gestart.

8. Type het test nummer in.
9. Ga nu naar de map ``executie_logs`` en open het bestand ``executie_testnummer.log`` met kladblok.
10. Kijk of er geen errors in dit bestand staan. Zodra dit het geval is kan je doorgann naar de volgende stap. De errors kan je herkennen aan het woord error.
    Er wordt ook informatie gegeven, hier staat het woord info voor en die zijn niet erg. Zodra er 
wel een error staat, moet de deze error opzoeken in dit readme bestand en kijken hoe je de error moet oplossen. Zodra je deze
    error hebt opgelost moet je cmd afsluiten en opnieuw terug gaan naar stap 5 en alles vanaf daar opnieuw doen.
    
11. Om het beeldscherm om te draaien klik je met rechtermuisknop op je bureaublad. Klik vervolgens op ``Beelscherminstellingen``.
12. Verander ``Schermstand`` van ``Liggend`` naar ``Liggend (gespiegeld)`` en druk vervolgens op ``Wijziging behouden``
    
13. Nu kan je terug gaan naar het executie scherm en de executie uitvoeren. **Let erop dat je geluid aan staat.**
   
   


# Errors executie
In de map ``executie_logs`` kan je alle log bestanden vinden van de executies, ze zijn genummerd op afleveringnummer.
In een log bestand kan je precies zien wat het programma heeft uitgevoerd en of er een error is geweest.
Elke regel geeft informatie over een onderdeel van het programma. Het volgende format wordt gehanteerd: datum - info/error - bericht.
``Info/error`` geeft aan of het er een error heeft plaatsgevonden, de ``info`` tag betekent dat ìets goed verlopen is. Zodra er
error staat betekent dit dat er iets niet goed verlopen is. Zodra dit het geval is kan je het bericht kopiëren en opzoeken
in deze readme. Deze readme geeft dan precies aan welke stappen je moet ondernemen om de error op te lossen.

### Het bestand van ``inlognaam`` ontbreekt in de map losse_csv
Dit kan twee dingen betekenen:
1. Het inlognamen bestand klopt niet. Dit betekent dat hier een laptop naam in staat die niet gebruikt is voor de huidige
test. Dit los je op door in het bestand inlognamen onder elkaar alleen de namen te zetten van de laptops waarop
   de huidige test gemaakt is.
   
2. Het bestand van de laptop met de ``inlognaam`` ontbreekt in de map ``losse_csv``. Dit is op te lossen door het bestand
van de laptop van ``inlognaam`` op de usb-stick te zetten en vervolgens op jouw laptop te zetten.
   
### De volgende mensen hebben twee keer de test gemaakt:
Dit betekent dat de mensen die geprint worden de test twee keer gemaakt hebben. Dit kan je oplossen
door naar de map ``losse_csv`` te gaan en in alle csv bestanden van dat quiz nummer te kijken waar die persoon dubbel in staat.
Vervolgens verwijder je een van die regels uit het bestand en dat heeft diegene de test maar 1 keer gemaakt.

### ``persoon`` zit in het spel maar heeft de test nog niet gemaakt
Dit kan twee redenen hebben:
1. De persoon moet de test nog maken. Dit kan je doen door de test opnieuw te openen op jouw laptop en die persoon hem
nog laten maken op jouw laptop.
   
2. Het bestand ``jokers_vrijstellingen`` klopt niet. Je kan dit oplossen door de persoon die uit het spel ligt en die toch aangegeven
wordt als in het spel uit het bestand ``jokers_vrijstellingen.txt`` te halen.
   
### De volgende mensen hebben de test gemaakt terwijl ze uit het spel liggen:
Dit kan drie redenen hebben:
1. Iemand heeft de test gemaakt maar die persoon ligt uit het spel. Dit kan je oplossen door naar de csv van de bijbehorende test te gaan in de map
``losst_csv`` en de regel van die persoon uit de csv te halen. Nu kan je de executie code opnieuw uitvoeren.
   
2. Het ``jokers_vrijstellingen.txt`` bestand klopt niet. Deze kan je openen en de naam van de persoon erbij typen.

3. Iemand heeft zijn naam verkeerd getypt. Dit kan je oplossen door naar de csv in het mapje ``losse_csv`` te gaan en daar de
verkeerd getypte naam te veranderen zodat die goed gespeld is. 
   




### Het lettertype is niet hetzelfde als bij het televisie programma.
Dit betekent dat de font niet is geinstalleerd op de laptop. Doe dit door het bestand ``OCRAEXT.TTF`` te openen
en op installeren te drukken. 

### Het groene scherm, rode scherm of het afvaller muziekje ontbreekt.
Dit betekent dat een of meerdere van die bestanden ontbreekt. Controleer of in de map ``Executie`` de bestanden
``Groen_echte_final.mp4`` en ``Rood_1.mp4`` aanwezig zijn. Als die er niet zijn moeten die bestanden erop gezet
worden vanaf de usb-stick. Controleer vervolgens of het bestand ``afvaller_muziek.mp3`` in de hoofdmap van het project staat

### ``persoon`` heeft de test niet gemaakt

Dit betekent dat de naam die is ingevoerd in het venster niet voorkomt in de csv.
Dit kan dus betekenen dat je de naam verkeerd hebt getypt of dat die persoon zijn/haar naam bij het maken van de test verkeerd heeft ingetypt.
Dit kan je oplossen door naar de csv van de test te gaan in de map ``losse_csv`` en de naam daar aan te passen.

### Het bestand ``path`` ontbreekt
Dit betekent dat je het bestand met het pad ``path`` in de hoofdmap van het project moet zetten.
Deze staat op de usb-stick in de map ``widm`` op de locatie die ``path`` aangeeft.

### Het bestand jokers_vrijstelling.txt ontbreekt.
Dit los je op door het bestand ``jokers_vrijstellingen.txt`` van de usb-stick af te halen en in de hoofdmap
van het project te zetten. Deze open je vervolgens en dan haal je alle namen uit het bestand van de mensen die
uit het spel liggen. Sla vervolgens het bestand op.  

### Muziek niet aanwezig
De muziek file staat niet op de goede plaats. Controleer of "test_muziek.wav" in de map "widm" staat. 
Zo niet dan moet je die even via de usb stick van jou laptop kopieëren

### In het geval dat de test bij een persoon uitvalt tijdens het maken.
Zodra een computer uitvalt of om de een of andere reden valt het programma uit. maak dan een back-up van de bestanden
``tijdelijke_opslag.txt``. Laat vervolgens diegene waarbij de test fout ging de test
opnieuw maken. Nadat iedereen de test gemaakt ga je naar de computer waarop diegene waarbij het fout ging de test gemaakt
heeft. In de map van het project verwijder je het bestand ``tijdelijke_opslag.txt`` en plaats je het bestand dat je gebackupt hebt.
Deze moet ook de naam hebben ``tijdelijke_opslag.txt``. Vervolgens type je in de zoekbalk in de map van het programma ``cmd`` en je drukt op enter.
Nu type je in cmd het volgende: ``py In_geval_van_crash.py afleveringnummer naam``, waar afleveringnummer het nummer van de aflevering is waarbij het fout ging
en naam is de naam van de persoon waarbij het fout ging. Druk vervolgens op enter en alles wordt gefixt. Nu kan je gwn normaal de stappen van de executie uitvoeren.


