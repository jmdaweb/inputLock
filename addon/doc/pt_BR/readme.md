# Bloqueio de Entrada (Input Lock) #

* Autor: José Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Baixe a [versão estável][1]

## Introdução

Você tem filhos ou animais de estimação em casa? Tem um gato e ele adora
subir na sua mesa e passear  pelo seu teclado? Você acidentalmente move o
mouse para partes aleatórias da tela enquanto usa seu laptop? Então o
Bloqueio de Entrada é para você! Poderá deixar o seu computador sozinho e
ligado sem correr riscos.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Modo de uso

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Quando pressiona o comando de bloqueio da entrada, o NVDA dirá "Entrada
bloqueada". Os seus dispositivos de entrada serão bloqueados até que
pressione o mesmo comando novamente. Nesse momento, o NVDA dirá "Entrada
desbloqueada" e tudo funcionará normalmente.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Se pressionar o comando de bloqueio do mouse, o mouse será
bloqueado. Pressione este comando novamente para o desbloquear. Com o mouse
bloqueado, pode usar os comandos do NVDA para movê-lo e clicar com os botões
esquerdo e direito, mas não pode mover o mouse sozinho. Os cliques do mouse
também podem ser desabilitados na categoria Bloqueio de entrada no diálogo
de configurações do NVDA (NVDA 2018.2 e posterior) ou no diálogo de
configurações de complementos das versões mais antigas, disponível no menu
de preferências. Além disso, a partir dessas configurações, pode controlar
os bloqueios do mouse quando o NVDA é iniciado ou não.

Nota: quando os cliques do mouse estão bloqueados, não pode usar nenhum
comando do NVDA para trabalhar com o mouse.

## Limitações e problemas conhecidos

Bloqueio de Entrada tem os seguintes problemas conhecidos:

* Os atalhos control+alt+del e windows+l podem ser usados mesmo quando o
  teclado está bloqueado.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Registro de mudanças (Changelog)

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Adicionado sinalizadores (flags) de compatibilidade com as versões
  recentes do NVDA.
* Traduções atualizadas.

### Version 1.11

* Adicionado sinalizadores (flags) de compatibilidade com as versões
  recentes do NVDA.
* Traduções atualizadas.
* Now, minimum supported version is 2022.4.

### Version 1.10

* Adicionado sinalizadores (flags) de compatibilidade com as versões
  recentes do NVDA.
* Traduções atualizadas.
* Documentação atualizada.
* Now, minimum supported version is 2021.3.
* The input will remain blocked after waking up from standby mode. Thanks to
  Javi Dominguez.

### Versão 1.9

* Adicionado sinalizadores (flags) de compatibilidade com as versões
  recentes do NVDA.
* Traduções atualizadas.
* Documentação atualizada.

### Versão 1.8

* Adicionado sinalizadores (flags) de compatibilidade com as versões
  recentes do NVDA.
* Traduções atualizadas.

### Versão 1.7

* Adicionado sinalizadores (flags) de compatibilidade com as versões
  recentes do NVDA.
* Traduções atualizadas.

### Versão 1.6

* Agora, as configurações são removidas somente quando o complemento é
  desinstalado. A configuração não é mais redefinida durante a atualização.
* Traduções novas e atualizadas.

### Versão 1.5

* Acrescentada compatibilidade com as versões recentes do NVDA.
* Novas traduções.

### Versão 1.4

* Os comandos do complemento não são atribuídos por padrão.

### Versão 1.3

* Adicionado um painel de configuração na caixa de diálogo de
  configurações. Para versões antigas do NVDA, um item de menu e um diálogo
  também foram acrescentados.
* Adicionada uma configuração para bloquear o mouse, quando o NVDA é
  iniciado.
* Adicionada uma configuração para bloquear também os cliques do mouse
  enquanto o mouse estiver bloqueado.
* Pequenas falhas corrigidas, algumas otimizações de código e menos
  mensagens (strings) duplicadas para os tradutores

### Versão 1.2

* Agora, o mouse também pode ser bloqueado
* Novo comando para bloquear e desbloquear apenas o mouse

### Versão 1.1

* Se outro complemento tiver adicionado anteriormente uma função de captura
  ao inputManager, ela será restaurada quando a entrada for desbloqueada.

### Versão 1.0

* Versão inicial

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
