# Bloqueio de entrada #

* Autor: José Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Baixar [versão estável][1]

## Introdução

Tem filhos ou animais de estimação em casa? Tem um gato que adora trepar
para a sua mesa e passear  pelo seu teclado? Acidentalmente move o rato para
partes aleatórias no ecrã, enquanto usa o seu computador? Então o "Bloqueio
de entrada" é para si! A partir de agora, poderá deixar o seu computador
sozinho e ligado sem correr riscos.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Modo de uso:

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Quando pressiona o comando de bloqueio da entrada, o NVDA dirá "Entrada
bloqueada". Os seus dispositivos de entrada serão bloqueados até que
pressione o mesmo comando novamente. Nesse momento, o NVDA dirá "Entrada
desbloqueada" e tudo funcionará como de costume.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Se pressionar o comando de bloqueio do rato, o rato será
bloqueado. Pressione este comando novamente para o desbloquear. Com o rato
bloqueado, pode usar os comandos do NVDA para movê-lo e clicar com os botões
esquerdo e direito, mas não pode mover o rato sozinho. Os cliques do rato
também podem ser desabilitados na categoria Bloqueio de entrada na caixa de
diálogo de configurações do NVDA (NVDA 2018.2 e posterior) ou na caixa de
diálogo de configurações adicionais das versões mais antigas, disponível no
menu de preferências. Além disso, a partir dessas configurações, pode
controlar os bloqueios do rato quando o NVDA é iniciado ou não.

Nota: quando os cliques do rato estão bloqueados, não pode usar nenhum
comando do NVDA para trabalhar com o rato.

## Limitações e problemas conhecidos

Este extra tem os seguintes problemas conhecidos:

* Os atalhos control+alt+del e windows+l podem ser usados mesmo quando o
  teclado está bloqueado.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Mudanças:

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Adicionadas etiquetas de compatibilidade com as versões recentes do NVDA
* Actualização de traduções

### Version 1.11

* Adicionadas etiquetas de compatibilidade com as versões recentes do NVDA
* Actualização de traduções
* Now, minimum supported version is 2022.4.

### Version 1.10

* Adicionadas etiquetas de compatibilidade com as versões recentes do NVDA
* Actualização de traduções
* Documentação actualizada.
* Now, minimum supported version is 2021.3.
* The input will remain blocked after waking up from standby mode. Thanks to
  Javi Dominguez.

### Versão 1.9

* Adicionadas etiquetas de compatibilidade com as versões recentes do NVDA
* Actualização de traduções
* Documentação actualizada.

### Versão 1.8

* Adicionadas etiquetas de compatibilidade com as versões recentes do NVDA
* Actualização de traduções

### Versão 1.7

* Adicionadas etiquetas de compatibilidade com as versões recentes do NVDA
* Actualização de traduções

### Versão 1.6

* Agora, as configurações são removidas somente quando o extra é
  desinstalado. A configuração não é mais redefinida durante a actualização.
* Foram adicionadas Novas traduções e outras sofreram actualizações:

### Versão 1.5

* Acrescentada compatibilidade com as versões recentes do NVDA
* Novas traduções:

### Versão 1.4

* Os comandos do extra não foram atribuídos, por padrão.

### Versão 1.3

* Adicionado um painel de configuração na caixa de diálogo de
  configurações. Para versões antigas do NVDA, um item de menu e um diálogo
  também foram acrescentados.
* Adicionada uma configuração para bloquear o rato, quando o NVDA é
  iniciado.
* Adicionada uma configuração para bloquear também os cliques do rato
  enquanto o rato estiver bloqueado.
* Pequenos bugs corrigidos, algumas optimizações de código e menos strings
  duplicadas para os tradutores

### Versão 1.2

* Agora, o rato também pode ser bloqueado.
* Novo comando para bloquear e desbloquear apenas o rato.

### Versão 1.1

* Se outro addon tiver adicionado anteriormente uma função de captura ao
  inputManager, ele será restaurado quando a entrada for desbloqueada.

### Versão 1.0

* Versão inicial

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
