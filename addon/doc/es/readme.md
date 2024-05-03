# Input Lock #

* Autor: José Manuel Delicado
* Compatibilidad con NVDA: de 2023.3.4 en adelante
* Descargar [versión estable][1]

## Introducción

¿Tienes niños o mascotas en casa? ¿Tienes un gato al que le gusta escalar la
mesa y pasearse por encima de tu teclado? ¿Mueves el ratón accidentalmente a
zonas aleatorias de la pantalla mientras usas el portátil? Entonces ¡Input
Lock es lo que necesitas! Podrás dejar el ordenador solo y encendido sin
riesgo.

Una vez instalado, podrás bloquear el teclado, la pantalla táctil (si tu
portátil tiene una), el panel táctil, el ratón y la pantalla Braille.

## Instrucciones de uso

Este complemento añade tres órdenes extra a NVDA. Por defecto vienen sin
asignar, así que tendrás que configurarlas desde el diálogo Gestos de
entrada. Lee la guía de usuario de NVDA para más información.

Cuando pulses la orden de alternar bloqueo de entrada, NVDA dirá "Entrada
bloqueada". Tus dispositivos de entrada se bloquearán hasta que pulses la
orden otra vez. En ese momento NVDA dirá "Entrada desbloqueada" y todo
volverá a funcionar como siempre.

Bloquear el panel táctil puede evitarnos tocarlo accidentalmente,
especialmente en aquellos casos donde se usa directamente el teclado del
portátil. Cuando pulses la orden de alternar bloqueo de panel táctil, NVDA
dirá "Panel táctil bloqueado". El panel táctil se bloqueará hasta que pulses
la orden otra vez. En ese momento NVDA dirá "Panel táctil desbloqueado" y
todo volverá a funcionar como siempre.

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

## Limitaciones y problemas conocidos

Bloqueo de entrada tiene los siguientes problemas conocidos:

* Los atajos ctrl+alt+supr y windows+l se pueden usar incluso con el teclado
  bloqueado.
* En los gestos usados para bloquear el panel táctil, procura asignar gestos
  cuyas combinaciones tengan pocas teclas. Se recomienda usar NVDA+letras o
  números, control+teclas de función, etc.

## Registro de cambios

### Versión 1.13

* Ahora, la versión mínima soportada es la 2023.3.4.
* Traducciones actualizadas. A partir de la versión 1.13, no se modificará
  el registro de cambios cuando una nueva versión sólo incluya traducciones
  actualizadas.
* Se ha añadido un gesto (sin asignar por defecto) para bloquear o
  desbloquear el panel táctil.

### Versión 1.12

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA.
* Traducciones actualizadas.

### Versión 1.11

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA.
* Traducciones actualizadas.
* Ahora, la versión mínima soportada es la 2022.4.

### Versión 1.10

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA.
* Traducciones actualizadas.
* Actualizada la documentación.
* Ahora, la versión mínima soportada es la 2021.3.
* La entrada permanecerá bloqueada después de salir de la
  suspensión. Gracias a Javi Domínguez.

### Versión 1.9

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA.
* Traducciones actualizadas.
* Actualizada la documentación.

### Versión 1.8

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA.
* Traducciones actualizadas.

### Versión 1.7

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA.
* Traducciones actualizadas.

### Versión 1.6

* Ahora, los ajustes se eliminan sólo al desinstalar el complemento. La
  configuración ya no se restablece al actualizar.
* Nuevas traducciones y traducciones actualizadas.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
