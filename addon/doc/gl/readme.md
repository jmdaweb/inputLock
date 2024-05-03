# Input Lock #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Descargar [versión estable][1]

## Introdución

Tes nenos ou mascotas na casa? Tes un gato ao que lle gusta moito subirse á
túa mesa e pasear sobre o teu teclado? Moves accidentalmente o rato a partes
aleatorias da pantalla mentras usas o teu portátil? Entón Input Lock é para
ti! Poderás deixar o teu computador só e acendido sen risco.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Uso

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Cando premas o xesto toggle input lock (alternar bloqueo de entrada), NVDA
dirá "Input locked" ("entrada bloqueada"). Os teus dispositivos de entrada
bloquearanse ata que premas o mesmo xesto de novo. Nese momento, NVDA dirá
"Input unlocked" ("Entrada desbloqueada") e todo funcionará como de costume.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Se premes o xesto toggle mouse lock (alternar bloqueo do rato), bloquearase
o teu rato. Preme este comando novamente para desbloquealo. Mentres o rato
está bloqueado, podes utilizar xestos do NVDA para movelo, e facer click cos
botóns esquerdo e dereito, pero non podes mover o propio rato. Os clicks do
rato tamén poden deshabilitarse dende a categoría Input lock ("Bloqueo de
entrada") no diálogo de axustes do NVDA (NVDA 2018.2 e superior) ou dende o
diálogo de preferencias do complemento en versións máis antigas, dispoñible
baixo o menú de preferencias. Ademais, con estes axustes podes controlar se
o rato se bloqueará ou non cando NVDA se inicie.

Nota: cando os clicks do rato están bloqueados, non podes utilizar ningún
xesto de NVDA para traballar co rato.

## Limitacións e problemas coñecidos

Input Lock ten os seguintes problemas coñecidos:

* Os atallo control+alt+supr e windows+l pódense utilizar mesmo cando o
  teclado está bloqueado.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Rexistro de trocos

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Actualizadas as marcas de compatibilidade para versións recentes de NVDA.
* Traducións actualizadas.

### Versión 1.11

* Actualizadas as marcas de compatibilidade para versións recentes de NVDA.
* Traducións actualizadas.
* Agora, a versión mínima soportada é a 2022.4.

### Versión 1.10

* Actualizadas as marcas de compatibilidade para versións recentes de NVDA.
* Traducións actualizadas.
* Documentación actualizada.
* Agora, a versión mínima soportada é a 2021.3.
* A entrada seguirá bloqueada tras volver do modo de suspensión. Grazas a
  Javi Dominguez.

### Versión 1.9

* Actualizadas as marcas de compatibilidade para versións recentes de NVDA.
* Traducións actualizadas.
* Documentación actualizada.

### Versión 1.8

* Actualizadas as marcas de compatibilidade para versións recentes de NVDA.
* Traducións actualizadas.

### Versión 1.7

* Actualizadas as marcas de compatibilidade para versións recentes de NVDA.
* Traducións actualizadas.

### Versión 1.6

* Agora a configuración só se borra ao desinstalar o complemento, non ao
  actualizalo.
* Traducións novas e actualizadas.

### Versión 1.5

* Engadida compatibilidade con versións recentes de NVDA.
* Novas traducións.

### Versión 1.4

* Os xestos do complemento están sen asignar por defecto.

### Versión 1.3

* Engadido un panel de configuración no diálogo de opcións do NVDA. Para
  versións antigas de NVDA, engadíronse tamén un elemento de menú e un
  diálogo.
* Engadido unha opción para bloquear o rato cando NVDA se inicie.
* Engadida unha opción para bloquear tamén clicks do rato mentres o rato
  estea bloqueado.
* Aranxados pequenos erros, algunhas optimizacións de código e menos cadeas
  duplicadas para tradutores

### Versión 1.2

* Agora o rato tamén pode bloquearse
* Novo atallo para bloquear e desbloquear só o rato

### Versión 1.1

* Se outro complemento xa engadiu una función capture ao inputManager,
  restáurase cando se desbloquea a entrada.

### Versión 1.0

* Liberación inicial

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
