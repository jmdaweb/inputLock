# Input Lock #

* Autor: José Manuel Delicado
* Compatibilidad con NVDA: de 2017.3 a 2019.1
* Descargar [versión estable][1]

## Introducción

¿Tienes niños o mascotas en casa? ¿Tienes un gato al que le gusta escalar la
mesa y pasearse por encima de tu teclado? ¿Mueves el ratón accidentalmente a
zonas aleatorias de la pantalla mientras usas el portátil? Entonces ¡Input
Lock es lo que necesitas! Podrás dejar el ordenador solo y encendido sin
riesgo.

Una vez instalado, podrás bloquear el teclado, la pantalla táctil, si tu
portátil tiene una, el ratón y la pantalla Braille.

## Instrucciones de uso

Este complemento añade dos órdenes extra a NVDA. Por defecto vienen sin
asignar, así que tendrás que configurarlas desde el diálogo Gestos de
entrada. Lee la guía de usuario de NVDA para más información.

Cuando pulses la orden de alternar bloqueo de entrada, NVDA dirá "Entrada
bloqueada". Tus dispositivos de entrada se bloquearán hasta que pulses la
orden otra vez. En ese momento NVDA dirá "Entrada desbloqueada" y todo
volverá a funcionar como siempre.

Si pulsas la orden para alternar el bloqueo del ratón, se bloqueará tu
ratón. Pulsa otra vez esta orden para desbloquearlo. Mientras el ratón está
bloqueado, puedes usar gestos de NVDA para moverlo, y hacer clic con los
botones izquierdo y derecho, pero no puedes mover el ratón en sí. Los clics
del ratón también se pueden desactivar desde la categoría Ajustes de bloqueo
de entrada en el diálogo de opciones de NVDA (NVDA 2018.2 y posteriores) o
desde el diálogo de ajustes del complemento para versiones anteriores,
disponible en el menú preferencias. Además, desde estos ajustes puedes
controlar si el ratón se bloquea cuando se inicia NVDA o no.

Nota: cuando se bloquean los clics del ratón, no puedes usar ningún gesto de
NVDA para trabajar con el ratón.

## Limitaciones

Bloqueo de entrada tiene las siguientes limitaciones:

* El atajo ctrl+alt+supr se puede usar incluso con el teclado bloqueado.

## Registro de cambios

### Versión 1.5

* Añadida compatibilidad con versiones recientes de NVDA.
* Nuevas traducciones.

### Versión 1.4

* Los atajos del complemento están sin asignar por defecto.

### Versión 1.3

* Se ha añadido un panel de configuración en el diálogo de opciones. También
  se han añadido un diálogo y un elemento de menú para las versiones
  antiguas de NVDA.
* Se ha añadido un ajuste para bloquear el ratón cuando se inicia NVDA.
* Se ha añadido un ajuste para bloquear también los clics del ratón cuando
  el ratón está bloqueado.
* Pequeños fallos solucionados, algunas optimizaciones de código y menos
  cadenas duplicadas para los traductores

### Versión 1.2

* Ahora también se puede bloquear el ratón
* Nueva orden para bloquear y desbloquear sólo el ratón

### Versión 1.1

* Si otro complemento tiene una función de captura previamente agregada a
  inputManager, esta se restaura al desbloquear la entrada.

### Versión 1.0

* Versión inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
