# Eingabesperre #

* Autor: Jose Manuel Delicado
* NVDA-Kompatibilität: 2017.3 bis 2019.1
* [Stabile Version][1] herunterladen

## Einführung

Haben Sie Kinder oder Haustiere zu Hause? Haben Sie eine Katze, die sehr
gerne auf Ihren Tisch klettert und über Ihre Tastatur läuft? Bewegen Sie
versehentlich die Maus in zufällige Bereiche auf dem Bildschirm, während Sie
Ihren Laptop benutzen? Dann ist die Eingabesperre für Sie optimal! Sie
können Ihren Computer ohne Risiko eingeschaltet lassen, sodass Sie diesen
nicht beaufsichtigen müssen.

Nach der Installation werden Sie in der Lage sein, Ihre Tastatur, den
Touchscreen, Maus und auch die Braillezeile zu sperren.

## Verwendung

Diese Erweiterung fügt zwei zusätzliche Gesten für NVDA hinzu. Standardmäßig
sind Sie nicht zugeordnet, so dass Sie diese im Dialog
Eingaben... konfigurieren müssen. Für weitere Informationen lesen Sie das
NVDA-Benutzerhandbuch.

Wenn Sie die Tastenkombination zum Ein- / Ausschalten der Eingabesperre
drücken, sagt NVDA "Eingaben gesperrt". Es werden alle Eingabegeräte
gesperrt, bis Sie die gleiche Tastenkombination erneut drücken. In diesem
Moment sagt NVDA "Eingaben entsperrt" und alles wird wie gewohnt
funktionieren.

Wenn Sie den Befehl "Maus blockieren" ausführen, wird Ihre Maus
gesperrt. Führen Sie diesen Befehl erneut aus, um die Maus zu
entsperren. Während die Maus gesperrt ist, können Sie Funktionen von NVDA
verwenden, um Sie zu bewegen und links oder rechts klicken, aber Sie können
die Maus nicht selbst bewegen. Mausklicks können auch in der Kategorie
Input-Lock im NVDA-Einstellungsdialog (ab NVDA 2018.2) deaktiviert
werden. In älteren Versionen finden sich die Einstellungen im
Einstellungsdialog der Erweiterungen im Einstellungsmenü.

Darüber hinaus können Sie festlegen, ob die Maus beim Start von NVDA
automatisch gesperrt werden soll.

Hinweis: Wenn Mausklicks blockiert sind, können Sie keine NVDA-Funktionen
verwenden, um mit der Maus zu arbeiten.

## Einschränkungen

Die Eingabesperre hat folgende Einschränkungen:

* Die Tastenkombination Strg+Alt+Entfernen kann auch bei gesperrter Tastatur
  verwendet werden.

## Änderungen

### Version 1.6

* Now, settings are removed only when the add-on is
  uninstalled. Configuration is nolonger reset when upgrading.
* New and updated translations.

### Version 1.5

* Es wurde die Kompatibilität mit den neuesten NVDA-Versionen hinzugefügt.
* Neue Übersetzungen.

### Version 1.4

* Die Funktionen der Erweiterung sind standardmäßig keinen
  Tastenkombinationen zugeordnet.

### Version 1.3

* Im Einstellungsdialog wurde eine Einstellungskategorie hinzugefügt. Für
  alte NVDA-Versionen wurden auch ein Menüpunkt und ein Dialog hinzugefügt.
* Es wurde eine Einstellung hinzugefügt, um die Maus zu sperren, wenn NVDA
  gestartet wird.
* Es wurde eine Einstellung hinzugefügt, um auch Mausklicks zu blockieren,
  während die Maus gesperrt ist.
* Kleinere Fehlerbehebungen, einige Code-Optimierungen und weniger doppelte
  Zeichenketten für Übersetzer

### Version 1.2

* Nun kann die Maus auch gesperrt werden.
* Neue Tastenkombination, um die Maus zu sperren oder zu entsperren

### Version 1.1

* Wenn eine andere Erweiterung bereits auf die Eingabenverwaltung zugreift,
  wird der Zugriff wiederhergestellt, sobald die Eingabesperre aufgehoben
  wird.

### Version 1.0

* Erstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
