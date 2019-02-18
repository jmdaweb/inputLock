# Input Lock #

* Autore: Jose Manuel Delicado
* Compatibilità con NVDA: dalla 2017.3 alla 2019.1
* Scarica la [versione stabile][1]

## Introduzione:

Avete bambini o animali domestici in casa? Avete un gatto che ama
arrampicarsi sul vostro tavolo e passeggiare sulla tastiera? Spostate spesso
il mouse accidentalmente quando usate il vostro portatile? Allora Input Lock
è fatto per voi! Potrai lasciare il tuo computer acceso senza rischi.

Una volta installato, si potrà bloccare la tastiera, il mouse, il display
Braille e il touch screen se disponibile nel vostro portatile. 

## Utilizzo:

Questo componente consente l'utilizzo di due comandi extra per NVDA, di
default i comandi non sono assegnati, vedere la guida di NVDA per
informazioni sull'input dei gesti e tasti di immissione.

Premendo il comando assegnato per Input Lock, NVDA annuncierà Dispositivo di
immissione bloccato. I dispositivi di immissione resteranno quindi bloccati
finché non si premerà nuovamente lo stesso comando per sbloccare. In questo
secondo caso verrà annunciato Dispositivo di immissione sbloccato ed il
dispositivo riprenderà a funzionare come di consueto. 

Se si esegue il comando Attiva/disattiva blocco mouse, il mouse verrà
bloccato. Premere nuovamente lo stesso comando per sbloccare l'input del
mouse. Quando il mouse è bloccato sarà comunque possibile usare i comandi di
NVDA per muovere il puntatore o cliccare con i pulsanti del mouse, non sarà
però possibile spostare il puntatore tramite il dispositivo mouse. Inoltre,
dalle impostazioni di NVDA, sotto la categoria Input Lock, o nelle
impostazioni del componente aggiuntivo per le versioni precedenti a NVDA
2018.1, è possibile controllare la disattivazione dei clic del mouse. E'
anche possibile  impostare la disattivazione del mouse all'avvio di NVDA.

Nota: quando i clic del mouse son bloccati, non sarà possibile usare alcun
comando per il mouse con NVDA.

## Limitazioni

Input Lock ha le seguenti limitazioni:

* Il comando ctrl+alt+canc può essere utilizzato anche se la tastiera è
  bloccata.

## Changelog

### Version 1.7

* Updated compatibility flags for recent NVDA versions.
* Updated translations.

### Version 1.6

* Now, settings are removed only when the add-on is
  uninstalled. Configuration is nolonger reset when upgrading.
* New and updated translations.

### Version 1.5

* Aggiunta la compatibilità con le recenti versioni di NVDA. 
* Traduzioni aggiornate.

### Version 1.4

* I comandi non sono assegnati di default.

### Version 1.3

* Added a configuration panel in settings dialog. For old NVDA versions, a
  menu item and a dialog have been added too.
* Added a setting to lock the mouse when NVDA is started.
* Added a setting to block also mouse clicks while mouse is locked.
* Small bugs fixed, some code optimizations and less duplicated strings for
  translators

### Version 1.2

* Now the mouse can also be locked
* New command to lock and unlock only the mouse

### Version 1.1

* If another addon has previously added a capture function to inputManager,
  it is restored when the input is unlocked.

### Version 1.0

* Initial release

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
