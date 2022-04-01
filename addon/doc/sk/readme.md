# Blokovanie vstupu #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2021.3 and beyond
* Stiahnuť [stabilnú verziu][1]

## Úvod

Máte doma deti alebo domácich miláčikov? Často si náhodne presuniete myš a
potom píšete na nesprávne miesto? Doplnok blokovanie vstupu je práve pre
vás. Môžete bez obáv nechať váš počítač bez dozoru.

Doplnok umožňuje zablokovať klávesnicu, dotykovú obrazovku, myš aj
braillovský riadok.

## Použitie

Doplnok poskytuje dve nové klávesové skratky. Tieto predvolene nie sú
nastavené a je potrebné ich nastaviť v dialógu klávesové skratky. Návod na
používanie tejto funkcie nájdete v návode NVDA.

Ak stlačíte skratku na blokovanie vstupu, NVDA povie "vstup zamknutý" a
automaticky zablokuje vstup zo všetkých zariadení. Odblokovať ho môžete tou
istou klávesovou skratkou.

Druhá klávesová skratka umožňuje zamknúť len myš. Po zamknutí myši môžete s
kurzorom myši pracovať cez príkazy NVDA, nebudete ale môcť použiť fyzickú
myš. V nastaveniach doplnku môžete tiež aktivovať zamknutie klikania myši a
aktivovať °°automatické zamknutie myši po štarte NVDA.

Upozorňujeme, že ak povolíte zamknutie myši vrátane klikania, niektoré
funkcie NVDA nebudú fungovať.

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* On some laptops, the touchpad still accepts user input after mouse is
  blocked.

## Zmeny

### Version 1.10

* Upravené požiadavky kompatibility pre aktuálne verzie NVDA.
* Aktualizované preklady.
* Updated documentation.
* Now, minimum supported version is 2021.3.
* The input will remain blocked after waking up from standby mode. Thanks to
  Javi Dominguez.

### Version 1.9

* Upravené požiadavky kompatibility pre aktuálne verzie NVDA.
* Aktualizované preklady.
* Updated documentation.

### Verzia 1.8

* Upravené požiadavky kompatibility pre aktuálne verzie NVDA.
* Aktualizované preklady.

### Verzia 1.7

* Upravené požiadavky kompatibility pre aktuálne verzie NVDA.
* Aktualizované preklady.

### Verzia 1.6

* Nastavenia sa odteraz odstránia len po odinštalovaní doplnku. Pri
  aktualizácii doplnku ostanú zachované.
* Nové a aktualizované preklady.

### Verzia 1.5

* Upravené pre aktuálne verzie NVDA.
* Nové preklady.

### Verzia 1.4

* Klávesové skratky nie sú pridelené.

### Verzia 1.3

* Pridaný dialóg s nastaveniami v starších verziách NVDA a príslušná vetva
  do stromu s nastaveniami pre novšie verzie NVDA.
* Pridaná možnosť zablokovať myš automaticky po štarte NVDA.
* Pridaná možnosť zablokovať aj klikanie myšou.
* Drobné úpravy v kóde vrátane odstránených nadbytočných fráz na prekladanie

### Verzia 1.2

* Pridaná možnosť zamknúť myš
* Pridaná skratka na zamknutie a odomknutie myši

### Verzia 1.1

* Ak iný doplnok sleduje stav zariadenia, sledovanie sa obnoví po
  odblokovaní vstupu.

### Verzia 1.0

* Prvé vydanie

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
