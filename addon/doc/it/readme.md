# Input Lock #

* Autore: Jose Manuel Delicado
* NVDA compatibility: 2021.3 and beyond
* Scarica la [versione stabile][1]

## Introduzione

Avete bambini o animali domestici in casa? Avete un gatto che ama
arrampicarsi sul vostro tavolo e passeggiare sulla tastiera? Spostate spesso
il mouse accidentalmente quando usate il vostro portatile? Allora Input Lock
è fatto per voi! Potrete lasciare il vostro computer acceso senza rischi.

Una volta installato, si potrà bloccare la tastiera, il mouse, il display
Braille e il touch screen se disponibile nel vostro portatile.

## Utilizzo

Questo componente aggiunge due comandi extra per NVDA. Di default i comandi
non sono assegnati, perciò dovrete configurarli dalla finestra gesti e tasti
di immissione. Leggete il manuale utente di NVDA per ulteriori informazioni.

Premendo il tasto che attiva Input Lock, NVDA dirà "Dispositivo di
immissione bloccato". I dispositivi di immissione resteranno bloccati finché
non premerete nuovamente lo stesso tasto. A questo punto NVDA dirà
"Dispositivo di immissione sbloccato" e tutto funzionerà come sempre.

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
* On some laptops, the touchpad still accepts user input after mouse is
  blocked.

## Novità

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

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
