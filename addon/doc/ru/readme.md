# Input Lock #

* Автор: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Скачать [стабильную версию][1]

## Введение

У вас дома есть дети или домашние животные? У вас есть кошка, и она очень
любит лазить по вашему столу и ходить по клавиатуре? Вы случайно перемещаете
мышь в случайные части экрана во время использования ноутбука? Тогда
InputLock для вас! Вы сможете оставить свой компьютер в покое и без риска.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Использование

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Когда вы нажмете жест блокировки ввода, NVDA скажет "Ввод заблокирован. Ваши
устройства ввода будут заблокированы, пока вы снова не нажмете тот же
жест. В этот момент NVDA скажет "Ввод разблокирован", и все будет работать
как обычно.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Если вы нажмете жест блокировки мыши, ваша мышь будет заблокирована. Нажмите
эту команду еще раз, чтобы разблокировать его. Пока мышь заблокирована, вы
можете использовать жесты NVDA для ее перемещения и щелкать левой и правой
кнопками, но вы не можете перемещать саму мышь. Щелчки мышью также можно
отключить в категории Блокировка ввода в диалоговом окне настроек NVDA (NVDA
2018.2 и более поздние версии). или из диалогового окна настроек дополнения
для более старых версий, доступного в меню настроек. Кроме того, из этих
настроек вы можете контролировать, будет ли блокироваться мышь при запуске
NVDA или нет.

Примечание: когда щелчки мышью заблокированы, вы не можете использовать
жесты NVDA для работы с мышью.

## Ограничения и известные проблемы

InputLock имеет следующие известные проблемы:

* Комбинации клавиш control+alt+del и windows+l можно использовать даже при
  заблокированной клавиатуре.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Список изменений

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Обновлены флаги совместимости для последних версий NVDA.
* Обновлены переводы.

### Version 1.11

* Обновлены флаги совместимости для последних версий NVDA.
* Обновлены переводы.
* Now, minimum supported version is 2022.4.

### Версия 1.10

* Обновлены флаги совместимости для последних версий NVDA.
* Обновлены переводы.
* Обновлена ​​документация.
* Теперь минимальная поддерживаемая версия — 2021.3.
* Ввод останется заблокированным после выхода из режима ожидания. Спасибо
  Javi Dominguez.

### Версия 1.9

* Обновлены флаги совместимости для последних версий NVDA.
* Обновлены переводы.
* Обновлена ​​документация.

### Версия 1.8

* Обновлены флаги совместимости для последних версий NVDA.
* Обновлены переводы.

### Версия 1.7

* Обновлены флаги совместимости для последних версий NVDA.
* Обновлены переводы.

### Версия 1.6

* Теперь настройки удаляются только при удалении дополнения. Конфигурация
  больше не сбрасывается при обновлении.
* Новые и обновленные переводы.

### Версия 1.5

* Добавлена совместимость с последними выпусками NVDA.
* Новые переводы.

### Версия 1.4

* По умолчанию жесты дополнения не назначены.

### Версия 1.3

* Добавлена панель конфигурации в диалог настроек. Для старых версий NVDA
  также добавлен пункт меню и диалог.
* Добавлена настройка блокировки мыши при запуске NVDA.
* Добавлена настройка для блокировки щелчков мышью, когда мышь
  заблокирована.
* Исправлены небольшие ошибки, некоторые оптимизации кода и меньше
  дублированных строк для переводчиков

### Версия 1.2

* Теперь мышь также можно заблокировать
* Новая команда для блокировки и разблокировки только мыши

### Версия 1.1

* Если другой аддон ранее добавил функцию захвата в inputManager, она
  восстанавливается при разблокировке ввода.

### Версия 1.0

* Первый выпуск

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
