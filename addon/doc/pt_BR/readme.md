# Bloqueio de Entrada (Input Lock) #

* Autor: José Manuel Delicado
* Compatibilidade com NVDA: 2017.3 a 2021.1
* Baixe a [versão estável][1]

## Introdução

Você tem filhos ou animais de estimação em casa? Tem um gato e ele adora
subir na sua mesa e passear  pelo seu teclado? Você acidentalmente move o
mouse para partes aleatórias da tela enquanto usa seu laptop? Então o
Bloqueio de Entrada é para você! Poderá deixar o seu computador sozinho e
ligado sem correr riscos.

Uma vez instalado, você será capaz de bloquear o seu teclado, tela de toque,
se o seu laptop tiver uma, mouse e Linha Braille.

## Modo de uso

Este complemento adiciona dois comandos ao NVDA. Por padrão, eles não estão
atribuídos (não tem teclas de atalho), portanto, terá que configurá-los a
partir da caixa de diálogo Definir comandos. Leia o Guia do Usuário do NVDA
para mais informações.

Quando pressiona o comando de bloqueio da entrada, o NVDA dirá "Entrada
bloqueada". Os seus dispositivos de entrada serão bloqueados até que
pressione o mesmo comando novamente. Nesse momento, o NVDA dirá "Entrada
desbloqueada" e tudo funcionará normalmente.

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
* O NVDA desbloqueia o teclado e outros métodos de entrada quando o
  computador sai do modo de espera ou a sessão é restaurada a partir da tela
  de bloqueio do Windows.
* Nalguns laptops, o touchpad ainda aceita a entrada do usuário depois que o
  mouse é bloqueado.

## Registro de mudanças (Changelog)

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

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
