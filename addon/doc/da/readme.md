# Inputlås #

* Forfatter: Jose Manuel Delicado
* NVDA-kompatibilitet: 2021.3 og senere
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

## Begrænsninger og kendte problemer

Inputlås har følgende kendte problemer:

* Genvejene Ctrl+alt+del og windows+l kan bruges, selv når tastaturet er
  låst.
* På nogle bærbare computere accepterer touchpad'en stadig brugerinput,
  efter at musen er blokeret.

## Ændringslog

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

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
