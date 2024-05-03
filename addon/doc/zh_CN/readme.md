# 输入锁 #

* 作者: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* 下载 [稳定版][1]

## 介绍

你家里有小孩或宠物吗？你是否有一只喜欢爬桌子的猫？他喜欢在你的键盘上跳来跳去。亦或者，在你使用电脑时，可能会不小心移动了鼠标。那么，输入锁适合您，您可以在离开电脑时锁定键盘和鼠标。

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## 用法

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

当您按下锁定键盘的快捷键时，NVDA会朗读“键盘已锁定”。此时，您的键盘会被锁定，直到您再次按下相同的快捷键，NVDA会朗读“键盘已解锁”，一切恢复正常状态。

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

当您按下锁定鼠标的快捷键时，鼠标会被锁定。再次按相同的快捷键可以解锁。当鼠标被锁定时，您依然可以使用 NVDA
的手势移动鼠标，并使用左右按钮单击，但您无法移动鼠标本身来改变鼠标指针位置。也可以在 NVDA 的设置对话框（NVDA 2018.2
及更高版本）中的“输入锁”类别或旧版本的插件设置对话框中禁用鼠标单击。此外，您还可以设置在启动 NVDA 时自动锁定鼠标。

注意：当鼠标单击被禁用时，您无法使用任何和鼠标相关的 NVDA 手势。

## 限制和已知问题

输入锁具有以下已知问题：

* 即使键盘被锁定，也可使用Ctrl+ alt + del 和 Windows + L 快捷键。
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## 更新日志

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* 更新了最新的 NVDA 版本兼容性标志。
* 更新翻译。

### 版本 1.11

* 更新了最新的 NVDA 版本兼容性标志。
* 更新翻译。
* 目前，支持的最低NVDA版本为 2022.4。

### 版本1.10

* 更新了最新的 NVDA 版本兼容性标志。
* 更新翻译。
* 更新文档。
* 目前，支持的最低NVDA版本为 2021.3。
* 从睡眠模式恢复后，输入锁定模式会保持。感谢 Javi Dominguez。

### 版本1.9

* 更新了最新的 NVDA 版本兼容性标志。
* 更新翻译。
* 更新文档。

### 版本1.8

* 更新了最新的 NVDA 版本兼容性标志。
* 更新翻译。

### 版本1.7

* 更新了最新的 NVDA 版本兼容性标志。
* 更新翻译。

### 版本1.6

* 仅在卸载插件时才会删除设置。升级时，不会重置设置。
* 更新翻译。

### 版本1.5

* 与 NVDA 最新版兼容。
* 更新翻译。

### 版本1.4

* 默认情况下，插件手势未分配。

### 版本1.3

* 在设置对话框中添加了设置面板。对于旧版 NVDA 还添加了菜单项和设置对话框。
* 添加了在启动NVDA时锁定鼠标的设置。
* 添加了一个设置，可在鼠标锁定时禁用鼠标单击。
* 修复了小错误，优化了一些代码并减少了翻译人员的重复字符串

### 版本1.2

* 现在也可以锁定鼠标
* 用于锁定和解锁鼠标的新手势

### 版本1.1

* 如果另一个插件先前已向inputManager添加了捕获键盘输入功能，则在输入解锁时将恢复该功能。

### 版本1.0

* 发布初始版本

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
