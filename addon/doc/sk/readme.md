# Blokovanie vstupu #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Stiahnuť [stabilnú verziu][1]

## Úvod

Máte doma deti alebo domácich miláčikov? Často si náhodne presuniete myš a
potom píšete na nesprávne miesto? Doplnok blokovanie vstupu je práve pre
vás. Môžete bez obáv nechať váš počítač bez dozoru.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Použitie

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Ak stlačíte skratku na blokovanie vstupu, NVDA povie "vstup zamknutý" a
automaticky zablokuje vstup zo všetkých zariadení. Odblokovať ho môžete tou
istou klávesovou skratkou.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

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
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Zmeny

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Upravené požiadavky kompatibility pre aktuálne verzie NVDA.
* Aktualizované preklady.

### Version 1.11

* Upravené požiadavky kompatibility pre aktuálne verzie NVDA.
* Aktualizované preklady.
* Now, minimum supported version is 2022.4.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
