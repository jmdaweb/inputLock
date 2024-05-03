# Inputlås #

* Forfatter: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Download [stabil version][1]

## Introduktion

Har du børn eller kæledyr hjemme? Har du en kat, der godt kan lide at klatre
op på bordet og gå henover dit tastatur? Flytter du tilfældigt musen til
tilfældige dele på skærmen, mens du bruger din bærbare computer? Så er
Inputlås til dig! Du vil være i stand til at forlade din computer og tændt
uden risiko.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Brug

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Når du trykker på tastekombinationen der låser input, vil NVDA sige Input
låst". Dine inputenheder blokeres, indtil du trykker på samme taster
igen. NVDA vil nu sige "Input låst op" og alt fungerer som normalt.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Hvis du trykker på tasterne til at blokere musen, vil musen blive låst. Tryk
på denne kommando igen for at låse den op. Mens musen er låst, kan du bruge
NVDA-bevægelser til at flytte den og klikke med venstre og højre museknap,
men du kan ikke flytte selve musen. Museklik kan også deaktiveres fra
indstillingskategorien "Inputlås" i NVDAs indstillingsdialog (NVDA 2018.2 og
senere) eller fra tilføjelsesindstillingsdialogen for ældre versioner, der
findes under opsætingsmenuen. Derudover kan du fra disse indstillinger
kontrollere, hvorvidt musen automatisk låser når NVDA startes eller ej.

Bemærk: Når museklik er blokeret, kan du ikke bruge NVDA-bevægelser til at
arbejde med musen.

## Begrænsninger og kendte problemer

Inputlås har følgende kendte problemer:

* Genvejene Ctrl+alt+del og windows+l kan bruges, selv når tastaturet er
  låst.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Ændringslog

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.
* Opdaterede oversættelser.

### Version 1.11

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.
* Opdaterede oversættelser.
* Now, minimum supported version is 2022.4.

### Version 1.10

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.
* Opdaterede oversættelser.
* Opdateret dokumentation.
* Nu er den mindste understøttede version 2021.3.
* Input forbliver blokeret, når du vågner enheden fra standbytilstand. Tak
  til Javi Dominguez.

### Version 1.9

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.
* Opdaterede oversættelser.
* Opdateret dokumentation.

### Version 1.8

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.
* Opdaterede oversættelser.

### Version 1.7

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.
* Opdaterede oversættelser.

### Version 1.6

* Nu bliver indstillingerne kun fjernet, når tilføjelsen er
  afinstalleret. Konfigurationen nulstilles ikke længere ved opgradering.
* Nye og opdaterede oversættelser.

### Version 1.5

* Tilføjede kompatibilitet for seneste NVDA-versioner.
* Nye oversættelser.

### Version 1.4

* Tilføjelsens kommandoerer ikke tildelte som standard.

### Version 1.3

* Tilføjet et konfigurationspanel i indstillingsdialogboksen. For gamle
  NVDA-versioner er der også tilføjet et menupunkt og en dialogboks.
* Tilføjet en indstilling for automatisk at låse musen, når NVDA startes.
* Tilføjet en indstilling for at blokere museklik, mens musen er låst.
* Små fejlrettelser, nogle kodeoptimeringer og mindre duplikerede strenge
  til oversættere

### Version 1.2

* Nu kan musen også låses
* Ny kommando til at låse og låse op for musen

### Version 1.1

* Hvis en anden tilføjelse tidligere har tilføjet en capture-funktion til
  inputManager, gendannes den, når indgangen er låst op.

### Version: 1.0

* Første udgivelse

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
