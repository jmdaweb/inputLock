# Input Lock #

* Autor: Jose Manuel Delicado
* Zgodność z NVDA: 2022.4 i nowsze
* Pobierz [wersja stabilna][1]

## Opis

Masz w domu zwierzęta lub małe dzieci? Czy Twój kot uwielbia wspinać się na
Twoje biurko i spacerować po klawiaturze komputera? Czy korzystając z
laptopa, zdarza Ci się przesuwać kursor myszy w przypadkowe miejsca na
ekranie? Jeśli tak, to Input Lock jest właśnie dla Ciebie! Teraz możesz
pozostawić włączony komputer bez żadnego ryzyka.

Za pomocą tego dodatku możesz zablokować klawiaturę, ekran dotykowy (jeśli
Twój laptop taki posiada), mysz i monitor brajlowski.

## Jak używać

Input Lock dodaje do NVDA dwa nowe polecenia. Domyślnie są one
nieprzypisane, więc trzeba je skonfigurować w oknie dialogowym Zdarzenia
wejścia. Więcej informacji znajdziesz w Podręczniku Użytkownika NVDA.

Kiedy naciśniesz polecenie ustawione dla Przełączania urządzeń wejścia, NVDA
powie"Urządzenia wejścia zablokowane". Urządzenia wejścia będą zablokowane,
aż do ponownego naciśnięcia tego samego polecenia. NVDA powie wtedy
"Urządzenia wejścia odblokowane" i wszystko zacznie działać tak jak zawsze.

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
* Na niektórych laptopach touchpad nadal akceptuje dane wejściowe
  użytkownika po zablokowaniu myszy.

## Lista zmian

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
