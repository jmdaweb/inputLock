# Zaključaj unos (Input Lock) #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Preuzmi [stabilnu verziju][1]

## Uvod

Imaš djecu ili kućne ljubimce? Imaš mačku koja se voli popesti na stol i
hodati po tvojoj tipkovnici? Premještaš li slučajno miša po ekranu dok
koristiš laptop? „Zaključaj unos” rješava te probleme! Moći ćeš ostaviti
uključeno računalo bez rizika.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Primjena

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Kad se pritisne gesta za zaključavanje unosa, NVDA će reći „Unos
zaključan”. Unosi će biti blokirani, sve dok se ista gesta ne pritisne
ponovo. U tom trenutku, NVDA će reći „Unos otključan” i sve će raditi kao
obično.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Ako se pritisne gesta za blokiranje miša, miš će se zaključati. Ponovnim
pritiskom ove naredbe će se miš otključati. Dok je miš zaključan, miš se
može pokretati pomoću NVDA gesta i klikati s lijevom i desnom tipkom, ali
nije moguće pomaknuti samog miša. Klikanje miša se također može deaktivirati
u kategoriji „Zaključaj unos” u dijaloškom okviru NVDA postavki (NVDA 2018.2
i noviji) ili u dijaloškom okviru postavki dodatka za starije verzije,
dostupne putem izbornika postavki. Nadalje, u ovim postavkama je moguće
odrediti, hoće li miš biti zaključan kad se pokrene NVDA ili ne.

Napomena: kad je klikanje miša uključeno, nije moguće koristiti bilo koju
NVDA gestu za rad s mišem.

## Ograničenja i poznati problemi

„Zaključaj unos” ima sljedeće poznate probleme:

* Prečaci kontrol+alt+del i windows+l mogu se koristiti čak i kad je
  tipkovnica zaključena.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Promjene

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Ažurirani problemi kompatibilnosti za nedavne NVDA verzije.
* Ažurirani prijevodi.

### Verzija 1.11

* Ažurirani problemi kompatibilnosti za nedavne NVDA verzije.
* Ažurirani prijevodi.
* Sada je najmanja podržana verzija 2022.4.

### Verzija 1.10

* Ažurirani problemi kompatibilnosti za nedavne NVDA verzije.
* Ažurirani prijevodi.
* Ažurirana dokumentacija.
* Sada, najmanja podržana verzija je 2021.3.
* Mogućnost unosa će ostati blokirana nakon buđenja iz stanja
  pripravnosti. Hvala Javi Dominguezu.

### Verzija 1.9

* Ažurirani problemi kompatibilnosti za nedavne NVDA verzije.
* Ažurirani prijevodi.
* Ažurirana dokumentacija.

### Verzija 1.8

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

* Ako je jedan drugi dodatak prethodno dodao funkciju snimanja u upravljaču
  unosa, obnovit će se kad se mogućnost unosa otključa.

### Verzija 1.0

* Prvo izdanje

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
