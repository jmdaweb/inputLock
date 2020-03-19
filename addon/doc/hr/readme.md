# Zaključaj ulazne uređaje (Input Lock) #

* Autor: Jose Manuel Delicado
* NVDA kompatibilno: 2017.3 do 2019.1
* Preuzmi [stabilnu verziju][1]

## Uvod

Imaš djecu ili kućne ljubimce? Imaš mačku koja se voli popesti na stol i
hodati preko tvoje tipkovnice? Premještaš li slučajno miša po ekranu dok
koristiš laptop? „Zaključaj ulazne uređaje” rješava te probleme! Moći ćeš
ostaviti uključeno računalo bez rizika.

Nakon instaliranja je moguće zaključati tipkovnicu, dodirni ekran (ukoliko
ga laptop ima), miša i brajični redak.

## Primjena

Ovaj dodatak dodaje dvije geste NVDA čitaču. Standardno one nisu dodijeljene
te se moraju konfigurirati u dijaloškom okviru Ulazne geste. Korisnički
vodič za NVDA sadrži daljnje informacije.

Kad se pritisne gesta za zaključavanje ulaznog uređaja, NVDA će reći „Ulazni
uređaji zaključani”. Ulazni uređaji će biti blokirani, sve dok se ista gesta
ne pritisne ponovo. U tom trenutku, NVDA će reći „Ulazni uređaji otključani”
i sve će raditi kao obično.

Ako se pritisne gesta za blokiranje miša, miš će se zaključati. Ponovnim
pritiskom ove naredbe će se miš otključati. Dok je miš zaključan, miš se
može pokretati pomoću NVDA gesta i klikati s lijevom i desnom tipkom, ali
nije moguće pomaknuti samog miša. Klikanje miša se također može deaktivirati
u kategoriji „Zaključaj ulazne uređaje” u dijaloškom okviru NVDA postavki
(NVDA 2018.2 i noviji) ili u dijaloškom okviru postavki dodatka za starije
verzije, dostupne putem izbornika postavki. Nadalje, u ovim postavkama je
moguće odrediti, hoće li miš biti zaključan kad se pokrene NVDA ili ne.

Napomena: kad je klikanje miša uključeno, nije moguće koristiti bilo koju
NVDA gestu za rad s mišem.

## Ograničenja

„Zaključaj ulazne uređaje” ima sljedeća ograničenja:

* Prečac kontrol+alt+del je moguće koristiti čak i kad je tipkovnica
  uključena.

## Promjene

### Verzija 1.7

* Ažurirani problemi kompatibilnosti za nedavne NVDA verzije.
* Ažurirani prijevodi.

### Verzija 1.7

* Ažurirani problemi kompatibilnosti za nedavne NVDA verzije.
* Ažurirani prijevodi.

### Verzija 1.6

* Sada se uklanjanju postavke samo ako se dodatak deinstalira. Konfiguracija
  se neće resetirati prilikom nadogradnje.
* Novi i ažurirani prijevodi.

### Verzija 1.5

* Dodana kompatibilnost s nedavnim NVDA izdanjima.
* Novi prijevodi.

### Verzija 1.4

* Geste dodatka standardno nisu dodijeljenje.

### Verzija 1.3

* Dodana je konfiguracijska ploča u dijaloškom okviru za postavke. Za stare
  NVDA verzije, stavka izbornika i dijalošli okvir su također dodani.
* Dodana je postavka za zaključavanje miša kad se NVDA pokrene.
* Dodana je postavka i za zaključavanje klikanja mišem dok je miš uključen.
* Popravak manjih grešaka, neka optimizacija koda i manje duplih znakovnih
  nizova za prijevode

### Verzija 1.2

* Sada je moguće zaključati i miša
* Nove naredbe za zaključavanje i otključavanje samo miša

### Verzija 1.1

* Ako je jedan drugi dodatak prethodno dodao funkciju za snimanje u
  upravljaču ulaznih uređaja, bit će obnovljen, kad se ulazni uređaji
  otključaju.

### Verzija 1.0

* Prvo izdanje

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
