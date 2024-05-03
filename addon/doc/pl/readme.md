# Input Lock #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Pobierz [wersja stabilna][1]

## Opis

Masz w domu zwierzęta lub małe dzieci? Czy Twój kot uwielbia wspinać się na
Twoje biurko i spacerować po klawiaturze komputera? Czy korzystając z
laptopa, zdarza Ci się przesuwać kursor myszy w przypadkowe miejsca na
ekranie? Jeśli tak, to Input Lock jest właśnie dla Ciebie! Teraz możesz
pozostawić włączony komputer bez żadnego ryzyka.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Jak używać

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Kiedy naciśniesz polecenie ustawione dla Przełączania urządzeń wejścia, NVDA
powie"Urządzenia wejścia zablokowane". Urządzenia wejścia będą zablokowane,
aż do ponownego naciśnięcia tego samego polecenia. NVDA powie wtedy
"Urządzenia wejścia odblokowane" i wszystko zacznie działać tak jak zawsze.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Kiedy naciśniesz polecenie ustawione dla przełączania blokady myszy, mysz
zostanie zablokowana. Aby ją odblokować, naciśnij ponownie to samo
polecenie. Przy włączonej blokadzie myszy nadal można używać poleceń NVDA
służących do przemieszczania myszy i klikania lewym i prawym
przyciskiem. Nie da się jednak używać samej myszy. Kliknięcia myszy można
też wyłączyć w kategorii ustawień Input Lock w menu ustawień NVDA (NVDA
2018.2 i nowsze) lub w dialogu ustawień dodatków, który znajduje się w menu
Ustawienia, w starszych wersjach NVDA. Dodatkowo, w tych ustawieniach możesz
określić, czy mysz ma być automatycznie blokowana po starcie NVDa, czy nie.

Uwaga! Jeśli kliknięcia myszy są zablokowane, polecenia NVDA dotyczące myszy
również nie działają.

## Ograniczenia i znane problemy

Blokada wejścia ma następujące znane problemy:

* Skróty control+alt+del i windows+l mogą być używane nawet wtedy, gdy
  klawiatura jest zablokowana.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Lista zmian

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Dodano zgodność z najnowszymi wersjami NVDA.
* Zaktualizowane tłumaczenia.

### Wersja 1.11

* Dodano zgodność z najnowszymi wersjami NVDA.
* Zaktualizowane tłumaczenia.
* Teraz minimalna obsługiwana wersja to 2022.4.

### Wersja 1.10

* Dodano zgodność z najnowszymi wersjami NVDA.
* Zaktualizowane tłumaczenia.
* Zaktualizowana dokumentacja.
* Teraz minimalna obsługiwana wersja to 2021.3.
* Wejście pozostanie zablokowane po wybudzeniu z trybu
  gotowości. Podziękowania dla Javiego Domingueza.

### Wersja 1.9

* Dodano zgodność z najnowszymi wersjami NVDA.
* Zaktualizowane tłumaczenia.
* Zaktualizowana dokumentacja.

### Wersja 1.8

* Dodano zgodność z najnowszymi wersjami NVDA.
* Zaktualizowane tłumaczenia.

### Wersja 1.7

* Dodano zgodność z najnowszymi wersjami NVDA.
* Zaktualizowane tłumaczenia.

### Wersja 1.6

* Od teraz ustawienia usuwają się tylko po odinstalowaniu dodatku. Ponadto,
  nie resetują się już po aktualizacji.
* Nowe i zaktualizowane tłumaczenia.

### Wersja 1.5

* Dodana zgodność z ostatnimi wersjami NVDA.
* Nowe tłumaczenia.

### Wersja 1.4

* Polecenia dodatku są domyślnie nieprzypisane.

### Wersja 1.3

* Dodano panel ustawień w oknie dialogowym ustawień NVDA, jak również
  element menu i okno dialogowe dla starszych wersji NVDA.
* Dodano możliwość blokowania myszy przy starcie NVDA.
* Dodano możliwość blokowania kliknięć myszy, kiedy sama mysz jest już
  zablokowana.
* Naprawiono małe błędy, niektóre optymalizacje kodu i mniej zduplikowanych
  ciągów dla tłumaczy

### Wersja 1.2

* Teraz mysz może być również zablokowana
* Nowe polecenie blokowania i odblokowywania tylko myszy

### Wersja 1.1

* Jeżeli inny dodatek już wcześniej dodał funkcję przechwytywania do
  menedżera urządzeń wejścia, zostanie ona wznowiona gdy urządzenia wejścia
  zostaną odblokowane.

### Wersja 1.0

* Wersja pierwotna

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
