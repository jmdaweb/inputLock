# Zaključavanje unosa #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2022.4 and beyond
* Preuzmi [stabilnu verziju][1]

## Uvod

Imate decu ili kućne ljubimce u kući? Imate mačku koja voli da se penje po
vašem stolu i šeta po tastaturi? Da li slučajno pomerate vaš miš po delovima
ekrana dok koristite vaš laptop? Onda je dodatak zaključavanje unosa za v
as! Moćićete da ostavite vaš računar uključen bez rizika.

Nakon što je instaliran, moćićete da zaključate vašu tastaturu, ekran
osetljiv na dodir, ako ga vaš laptop ima, miš i brajev red.

## Korišćenje

Ovaj dodatak dodaje dve dodatne prečice u NVDA. Po podrazumevanim
podešavanjima one su nedodeljene, pa ih morate podesiti iz dijaloga ulazne
komande. Pročitajte NVDA korisničko uputstvo za više informacija.

Kada pritisnete prečicu koja uključuje i isključuje zaključavanje unosa,
NVDA će izgovoriti "unos zaključann". Vaši uređaji za unos će biti
zaključani dok ne pritisnete istu prečicu ponovo. U tom trenutku, NVDA će
izgovoriti "unos otključan" i sve će raditi kao i obično.

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
* On some laptops, the touchpad still accepts user input after mouse is
  blocked.

## Promene

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

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
