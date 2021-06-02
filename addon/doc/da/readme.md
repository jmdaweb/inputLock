# Inputlås #

* Forfatter: Jose Manuel Delicado
* NVDA compatibility: 2017.3 to 2021.1
* Download [stabil version][1]

## Introduktion

Har du børn eller kæledyr hjemme? Har du en kat, der godt kan lide at klatre
op på bordet og gå henover dit tastatur? Flytter du tilfældigt musen til
tilfældige dele på skærmen, mens du bruger din bærbare computer? Så er
Inputlås til dig! Du vil være i stand til at forlade din computer og tændt
uden risiko.

Når denne tilføjelse er installeret, vil du kunne låse dit tastatur,
touchskærm (hvis din bærbare computer har en), mus og punktdisplay.

## Brug

Denne tilføjelsespakke tilføjer to ekstra inputbevægelser til NVDA. Som
standard er de ikke tildelt, så det er nødvendigt at konfigurere dem fra
dialogen "Inputbevægelser". Læs NVDAs brugervejledning for yderligere
information.

Når du trykker på tastekombinationen der låser input, vil NVDA sige Input
låst". Dine inputenheder blokeres, indtil du trykker på samme taster
igen. NVDA vil nu sige "Input låst op" og alt fungerer som normalt.

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

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* NVDA unlocks the keyboard and other input methods when the computer wakes
  up from standby mode or the session is restored from the Windows lock
  screen.
* On some laptops, the touchpad still accepts user input after mouse is
  blocked.

## Ændringslog

### Version 1.9

* Opdaterede kompatibilitetsflag til nyere NVDA-versioner.
* Opdaterede oversættelser.
* Updated documentation.

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

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
