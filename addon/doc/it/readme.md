# Input Lock #

* Autore: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Scarica la [versione stabile][1]

## Introduzione

Avete bambini o animali domestici in casa? Avete un gatto che ama
arrampicarsi sul vostro tavolo e passeggiare sulla tastiera? Spostate spesso
il mouse accidentalmente quando usate il vostro portatile? Allora Input Lock
è fatto per voi! Potrete lasciare il vostro computer acceso senza rischi.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Utilizzo

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Premendo il tasto che attiva Input Lock, NVDA dirà "Dispositivo di
immissione bloccato". I dispositivi di immissione resteranno bloccati finché
non premerete nuovamente lo stesso tasto. A questo punto NVDA dirà
"Dispositivo di immissione sbloccato" e tutto funzionerà come sempre.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Se si esegue il comando Attiva/disattiva blocco mouse, il mouse verrà
bloccato. Premere nuovamente lo stesso comando per sbloccarlo. Quando il
mouse è bloccato sarà comunque possibile usare i comandi di NVDA per muovere
il puntatore o cliccare con i pulsanti sinistro e destro del mouse, ma non
sarà possibile spostare il puntatore tramite il mouse stesso. E' inoltre
possibile disattivare i clic del mouse, dalle impostazioni di NVDA, sotto la
categoria Input Lock, o dalle impostazioni del componente aggiuntivo nel
menu Preferenze per le versioni precedenti a NVDA 2018.2. E' anche possibile
impostare la disattivazione del mouse all'avvio di NVDA.

Nota: quando i clic del mouse sono bloccati, non sarà possibile usare alcun
comando per lavorare con il mouse con NVDA.

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Novità

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Aggiunti i flag di compatibilità per le versioni nuove di NVDA.
* Traduzioni aggiornate.

### Version 1.11

* Aggiunti i flag di compatibilità per le versioni nuove di NVDA.
* Traduzioni aggiornate.
* Now, minimum supported version is 2022.4.

### Version 1.10

* Aggiunti i flag di compatibilità per le versioni nuove di NVDA.
* Traduzioni aggiornate.
* Updated documentation.
* Now, minimum supported version is 2021.3.
* The input will remain blocked after waking up from standby mode. Thanks to
  Javi Dominguez.

### Version 1.9

* Aggiunti i flag di compatibilità per le versioni nuove di NVDA.
* Traduzioni aggiornate.
* Updated documentation.

### Novità nella versione 1.8

* Aggiunti i flag di compatibilità per le versioni nuove di NVDA.
* Traduzioni aggiornate.

### Novità nella versione 1.7

* Aggiunti i flag di compatibilità per le versioni nuove di NVDA.
* Traduzioni aggiornate.

### Novità nella versione 1.6

* Ora le impostazioni vengono rimosse solo quando l'add-on viene
  disinstallato. Quando si effettua un aggiornamento, la configurazione non
  viene reimpostata.
* Traduzioni nuove e aggiornate.

### Novità nella versione 1.5

* Aggiunta la compatibilità con le versioni nuove di NVDA.
* Nuove traduzioni.

### Novità nella versione 1.4

* Per default, i comandi dell'add-on non sono assegnati ad alcun tasto.

### Novità nella versione 1.3

* Aggiunto un pannello di configurazione nella finestra impostazioni di
  NVDA. Sono anche stati aggiunti un elemento di menu e una finestra di
  dialogo, per le versioni vecchie.
* Aggiunta un'impostazione per bloccare il mouse all'avvio di NVDA.
* Aggiunta un'impostazione per bloccare anche i clic del mouse quando il
  mouse è bloccato.
* Corretti piccoli errori, qualche ottimizzazione al codice e meno stringhe
  duplicate per i traduttori

### Novità nella versione 1.2

* Ora anche il mouse può essere bloccato
* Nuovo comando per bloccare e sbloccare solo il mouse

### Novità nella versione 1.1

* Se un altro add-on ha aggiunto in precedenza una funzione di cattura al
  gestore dell'input, questa viene ripristinata quando l'input viene
  sbloccato.

### Novità nella versione 1.0

* Versione iniziale

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
