# Bloqueio de entrada #

* Autor: José Manuel Delicado
* Baixar [versão estável][1]

## Introdução

Tem filhos ou animais de estimação em casa? Tem um gato que adora trepar
para a sua mesa e passear  pelo seu teclado? Acidentalmente move o rato para
partes aleatórias no ecrã, enquanto usa o seu computador? Então o "Bloqueio
de entrada" é para si! A partir de agora, poderá deixar o seu computador
sozinho e ligado sem correr riscos.

Uma vez instalado este extra, será capaz de bloquear o seu teclado, o ecrã
táctil, se o seu computador o tiver, o rato e a linha Braille.

## Modo de uso:

Este extra adiciona dois comandos (teclas de atalho)ao NVDA. Por defeito, ,
eles não são atribuídos, portanto, terá que configurá-los a partir da caixa
de diálogo "entrada de comandos". Leia o Guia do utilizador do NVDA para
mais informações.

Quando pressiona o comando de bloqueio da entrada, o NVDA dirá "Entrada
bloqueada". Os seus dispositivos de entrada serão bloqueados até que
pressione o mesmo comando novamente. Nesse momento, o NVDA dirá "Entrada
desbloqueada" e tudo funcionará como de costume.

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

## Limitações:

Este extra tem as seguintes limitações:

* A tecla de atalho "control+alt+del" pode ser usada mesmo que o teclado
  esteja bloqueado.

## Mudanças:

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

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
