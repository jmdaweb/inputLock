# 输入锁 #

* 作者: Jose Manuel Delicado
* NVDA compatibility: 2017.3 to 2021.1
* 下载 [稳定版][1]

## 介绍

你家里有小孩或宠物吗？你有一只喜欢爬桌子和走在你的键盘上的猫吗？使用笔记本电脑时，是否会意外将鼠标移动到屏幕中的随机部分？输入锁适合您！可以放心地暂时离开电脑了。

安装完成后，您就可以锁定键盘和触摸屏，如果您的笔记本电脑配有鼠标和盲文显示器也可以锁定鼠标和盲文显示器。

## 用法

这个插件为NVDA添加了两个额外的手势。默认情况下，它们是未分配的，因此您必须从“输入手势”对话框中进行配置。有关更多信息，请阅读“NVDA用户指南”。

当您按下手势键盘锁开关时，NVDA将朗读“键盘已锁定”。您的键盘设备将被阻止，直到您再次按相同的手势。在那一刻，NVDA会朗读“键盘解锁”，一切都会照常运作。

如果按下手势鼠标锁开关，鼠标将被锁定。再次按此命令将其解锁。当鼠标被锁定时，您可以使用NVDA手势移动它，并使用左右按钮单击，但您无法移动鼠标本身。也可以在NVDA设置对话框（NVDA
2018.2和更高版本）中的输入锁定类别或旧版本的加载项设置对话框中禁用鼠标单击，可在首选项菜单下找到。此外，通过这些设置，您可以在启动NVDA时控制更少的鼠标锁定。

注意：当鼠标单击被阻止时，您无法使用任何和鼠标相关的NVDA手势。

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* NVDA unlocks the keyboard and other input methods when the computer wakes
  up from standby mode or the session is restored from the Windows lock
  screen.
* On some laptops, the touchpad still accepts user input after mouse is
  blocked.

## 更新日志

### Version 1.9

* 更新了最新NVDA版本的兼容性标志。
* 更新翻译。
* Updated documentation.

### 版本1.8

* 更新了最新NVDA版本的兼容性标志。
* 更新翻译。

### 版本1.7

* 更新了最新NVDA版本的兼容性标志。
* 更新翻译。

### 版本1.6

* 仅在卸载插件时才会删除设置。升级时，配置不再重置。
* 更新翻译。

### 版本1.5

* 兼容最新的NVDA版本。
* 新的翻译。

### 版本1.4

* 默认情况下，插件手势未分配。

### 版本1.3

* 在设置对话框中添加了配置面板。对于旧的NVDA版本，还添加了菜单项和对话框。
* 添加了在启动NVDA时锁定鼠标的设置。
* 添加了一个设置，可在鼠标锁定时阻止鼠标单击。
* 修复了小错误，一些代码优化和翻译器重复的字符串

### 版本1.2

* 现在鼠标也可以锁定
* 用于仅锁定和解锁鼠标的新命令

### 版本1.1

* 如果另一个插件先前已向inputManager添加了捕获键盘输入功能，则在输入解锁时将恢复该功能。

### 版本1.0

* 发布初始版本

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
