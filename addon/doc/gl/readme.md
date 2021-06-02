# Input Lock #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2017.3 to 2021.1
* Descargar [versión estable][1]

## Introdución

Tes nenos ou mascotas na casa? Tes un gato ao que lle gusta moito subirse á
túa mesa e pasear sobre o teu teclado? Moves accidentalmente o rato a partes
aleatorias da pantalla mentras usas o teu portátil? Entón Input Lock é para
ti! Poderás deixar o teu computador só e acendido sen risco.

Unha vez instalado, poderás bloquear o teu teclado, pantalla táctil, se o
teu portátil ten unha, rato e pantalla braille.

## Uso

Este complemento engade dous xestos extra a NVDA. Por defecto non están
asignados, de maneira que terás que configuralos dende o diálogo de Xestos
de entrada. Le a Guía do Usuario do NVDA para máis información.

Cando premas o xesto toggle input lock (alternar bloqueo de entrada), NVDA
dirá "Input locked" ("entrada bloqueada"). Os teus dispositivos de entrada
bloquearanse ata que premas o mesmo xesto de novo. Nese momento, NVDA dirá
"Input unlocked" ("Entrada desbloqueada") e todo funcionará como de costume.

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

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* NVDA unlocks the keyboard and other input methods when the computer wakes
  up from standby mode or the session is restored from the Windows lock
  screen.
* On some laptops, the touchpad still accepts user input after mouse is
  blocked.

## Rexistro de trocos

### Version 1.9

* Actualizadas as marcas de compatibilidade para versións recentes de NVDA.
* Traducións actualizadas.
* Updated documentation.

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

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
