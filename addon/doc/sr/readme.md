# Zaključavanje unosa #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Preuzmi [stabilnu verziju][1]

## Uvod

Imate decu ili kućne ljubimce u kući? Imate mačku koja voli da se penje po
vašem stolu i šeta po tastaturi? Da li slučajno pomerate vaš miš po delovima
ekrana dok koristite vaš laptop? Onda je dodatak zaključavanje unosa za v
as! Moćićete da ostavite vaš računar uključen bez rizika.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Korišćenje

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Kada pritisnete prečicu koja uključuje i isključuje zaključavanje unosa,
NVDA će izgovoriti "unos zaključann". Vaši uređaji za unos će biti
zaključani dok ne pritisnete istu prečicu ponovo. U tom trenutku, NVDA će
izgovoriti "unos otključan" i sve će raditi kao i obično.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Ako pritisnete prečicu koja uključuje i isključuje zaključavanje miša, Vaš
miš će biti zaključan. Pritisnite ovu komandu ponovo za njegovo
otključavanje. Dok je miš zaključan, možete koristiti NVDA prečice za
njegovo pomeranje, i  levi i desni klik, ali ne možete fizički pomerati
miš. Klikovi miša takođe mogu biti onemogućeni iz kategorije podešavanja
zaključavanja unosa u NVDA dijalogu za podešavanja (NVDA 2018.2 i noviji)
ili iz dijaloga za podešavanje dodatka u starijim verzijama, dostupan u
meniju podešavanja. Takođe, iz ovih podešavanja možete odabrati da li će se
miš zaključavati kada se NVDA pokrene.

Napomena: Kada su klikovi miša zaključani, ne možete koristiti nijednu NVDA
komandu za rad sa mišem.

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Promene

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Ažurirani parametri kompatibilnosti za najnovije NVDA verzije.
* Ažurirani prevodi.

### Version 1.11

* Ažurirani parametri kompatibilnosti za najnovije NVDA verzije.
* Ažurirani prevodi.
* Now, minimum supported version is 2022.4.

### Version 1.10

* Ažurirani parametri kompatibilnosti za najnovije NVDA verzije.
* Ažurirani prevodi.
* Updated documentation.
* Now, minimum supported version is 2021.3.
* The input will remain blocked after waking up from standby mode. Thanks to
  Javi Dominguez.

### Version 1.9

* Ažurirani parametri kompatibilnosti za najnovije NVDA verzije.
* Ažurirani prevodi.
* Updated documentation.

### Version 1.8

* Ažurirani parametri kompatibilnosti za najnovije NVDA verzije.
* Ažurirani prevodi.

### Verzija 1.7

* Ažurirani parametri kompatibilnosti za najnovije NVDA verzije.
* Ažurirani prevodi.

### Verzija 1.6

* Sada, podešavanja se uklanjaju samo kada je dodatak uklonjen. Podešavanja
  se više ne gube kada ažurirate dodatak.
* Novi i ažurirani prevodi.

### Verzija 1.5

* Dodata kompatibilnost sa najnovijim NVDA verzijama.
* Novi prevodi.

### Verzija 1.4

* Prečice dodatka su nedodeljene po podrazumevanim podešavanjima.

### Verzija 1.3

* Dodat panel sa podešavanjima za najnovije NVDA verzije. Za stare verzije,
  stavka u NVDA meniju je takođe dodata.
* Dodato podešavanje za zaključavanje miša kada se NVDA pokrene.
* Dodato podešavanje za sprečavanje klikova miša kada je miš zaključan.
* Male greške ispravljene, nekoliko optimizacija u kodu i manje duplih
  stavki za prevod.

### Verzija 1.2

* Sada miš takođe može biti zaključan
* Nova komanda za zaključavanje i otključavanje samo miša

### Verzija 1.1

* Ako je neki drugi dodatak dodao funkciju capture u inputManager, vraćena
  je kada se unos otključa.

### Verzija 1.0

* Prva verzija

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
