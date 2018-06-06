# Bloqueo de entrada
Versión 1.3

## Introducción

¿Tienes niños o mascotas en casa? ¿Tienes un gato al que le gusta escalar la mesa y pasearse por encima de tu teclado? ¿Mueves el ratón accidentalmente a zonas aleatorias de la pantalla mientras usas el portátil? Entonces ¡Input Lock es lo que necesitas! Podrás dejar el ordenador solo y encendido sin riesgo.

Una vez instalado, podrás bloquear el teclado, la pantalla táctil, si tu portátil tiene una, el ratón y la pantalla Braille.

## Modo de uso

Este complemento añade una orden extra a NVDA. Por defecto es NVDA+k, pero puede (y debería) cambiarse desde el diálogo Gestos de entrada. Lee la guía de usuario de NVDA para más información.

Cuando pulses esa orden, NVDA dirá "Entrada bloqueada". Tus dispositivos de entrada se bloquearán hasta que pulses la orden otra vez. En ese momento NVDA dirá "Entrada desbloqueada" y todo volverá a funcionar como siempre.

Si pulsas NVDA+shift+m, se bloqueará tu ratón. Pulsa otra vez esta orden para desbloquearlo. Por supuesto, puedes personalizarla desde el diálogo Gestos de entrada. Mientras el ratón está bloqueado, puedes usar gestos de NVDA para moverlo, y hacer clic con los botones izquierdo y derecho, pero no puedes mover el ratón en sí.

## Limitaciones

Bloqueo de entrada tiene las siguientes limitaciones:

* El atajo ctrl+alt+supr se puede usar incluso con el teclado bloqueado.

## Información de contacto

Este complemento ha sido desarrollado por José Manuel Delicado. Si quieres contactar conmigo, envía un e-mail a jm.delicado@nvda.es, o abre una incidencia en GitHub en https://github.com/jmdaweb/inputLock

## Registro de cambios

### Versión 1.2

* Ahora también se puede bloquear el ratón
* Nueva orden para bloquear y desbloquear sólo el ratón

### Versión 1.1

* Si otro complemento tiene una función de captura previamente agregada a inputManager, esta se restaura al desbloquear la entrada.

### Versión 1.0

* Versión inicial

