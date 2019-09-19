# Input Lock #

* Autor: Jose Manuel Delicado
* NVDA kompatibilno: 2017.3 do 2019.1
* Preuzmi [stabilnu inačicu][1]

## Uvod

Da li imate djecu ili kućne ljubimce doma? Da li imate mačku koja se veoma
voli penjati po vašem stolu i hodati preko vaše tipkovnice? Da li slučajno
premjestite miš  u dio ekrana za vrijeme korištenja vašeg laptopa? Stoga je
Input Lock za vas!  Bit će vam omogućeno samo napustiti vaše rač1nalo  i
uključiti ga bez rizika.

Jednim instaliranjem, Bit će vam omogućen pregled tipkovnice, dodir ekrana,
ako vaš laptop ima jedinicu, miša i Braille display.

## Korištenje

Ovaj dodatak dodaje dvije geste u NVDA. Po difoltu one nisu dodane, pa će te
ih morati konfigurirati   iz Input dijaloga s gestama. Čitaj NVDA Korisni
vodić za više informacija.

Kada pritisnete preklopnu input lock gestu, NVDA će reći "Input locked". Vaš
ulazni uređaj bit će blokiran dok ne pritisnete neku gestu ponovo. U tom
trenutku, NVDA će reći "Input unlocked" i sve će raditi kao obično.

Ako pritisnete prekidač miša blokiranu gestu, vaš miš bit će
uključen. Pritiskom ove kompande ponovo, on će biti isključen. Dok je miš
uključen, vi možete koristiti NVDA geste u pokretu, i klikati sa lijevom i
desnom tipkom, ali ga ne možete  pomaknuti. Klikanje miža također može biti
onemogućeno  iz Input lock kategorije u NVDA dijlogu postavki (NVDA 2018.2 i
kasnije) ili iz dijloga postavki dodataka za starije inačice, dostupne ispod
izbornika postavki. Nadalje, iz ovih postvki možete uključiti vremensku
kontrolu miša kad je NVDA započeo ili završio.

Bilješka: kada su klikovi miša uključeni, ne možete koristiti bilo koju NVDA
gestu za rad sa mišem.

## Ograničenja

Input Lock ima sljedeća ograničenja:

* Prečac control+alt+del može biti korišten čak i kad je tipkovnica
  uključena.

## Changelog

### Inačica 1.7

* Ažurirane kompatibilne zastve za nedavne NVDA inačice.
* Ažurirani prijevodi.

### Inačica 1.7

* Ažurirane kompatibilne zastve za nedavne NVDA inačice.
* Ažurirani prijevodi.

### Inačica 1.6

* Sada, su postavke uklonjene samo ako je dodatak
  deinstaliran. Konfiguracija se neće resetirati prilikom nadogradnje.
* Novi i ažurirani prijevodi.

### Inačica 1.5

* Dodana kompatibilnost sa nedavnim NVDA izdanja.
* Novi prijevodi.

### Inačica 1.4

* Dodane geste su  dodane po difoltu.

### Inačica 1.3

* Dodan konfiguracijski  panel u dijalog postavki. Za stare NVDA inačice,
  stavka izbornika i dijalog su dodani previše.
* Dodano u postavke uključivanje miša kad je NVDA pokrenut.
* Dodano u postavke  također blokiranje klikanje mišem dok je miš uključen.
* Popravak malih grešaka, neki code optimizcija i manji dupli nizovi za
  prijevode

### Inačica 1.2

* Sada miš također može biti
* Nove komande za uključivanje i isključivanje samo miša

### Inačica 1.1

* Ako sljedeći dodatak ima predhodno dodane funkcije za snimanje   u
  inputManager, to je obnovljeno kada je input isključen.

### Inačica 1.0

* Prvo izdanje

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
