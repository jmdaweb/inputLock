[[!meta title="Input Lock"]]

* Author: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Download [stable version][1]

## Introduction

Do you have kids or pets at home? Do you have a cat and It likes very much climbing your table and walking over your keyboard? Do you accidentally move the mouse to random parts in the screen while using your laptop? Then Input Lock is for you! You will be able to leave your computer alone and turned on without risk.

Once installed, you will be able to lock your keyboard, touch screen (if your laptop has one), touchpad, mouse and Braille display.

## Usage

This addon adds three extra gestures to NVDA. By default they are unassigned, so you will have to configure them from Input gestures dialog. Read the NVDA User Guide for more information.

When you press the toggle input lock gesture, NVDA will say "Input locked". Your input devices will be blocked until you press the same gesture again. In that moment, NVDA will say "Input unlocked" and everything will work as usual.
Locking the touchpad can prevent us from accidentally touching it, especially those who are used to using the laptop keyboard directly. When you press the toggle touchpad lock gesture, NVDA will say "Touchpad locked". Your touchpad will be blocked until you press the same gesture again. In that moment, NVDA will say "Touchpad unlocked" and everything will work as usual.

If you press the toggle mouse block gesture, your mouse will be locked. Press this command again to unlock it. While mouse is locked, you can use NVDA gestures to move it, and click with left and right buttons, but You can't move the mouse itself. Mouse clicks can also be disabled from Input lock category in NVDA settings dialog (NVDA 2018.2 and later) or from add-on settings dialog for older versions, available under preferences menu. In addition, from these settings you can control wether mouse locks when NVDA is started or not.

Note: when mouse clicks are blocked, you can't use any NVDA gestures to work with the mouse.

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the keyboard is locked.
* For gestures used to lock the touchpad, please try to assign a small number of key combination gestures. It is recommended to use NVDA+letters or numbers, Ctrl+F keys etc.

## Changelog

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Updated compatibility flags for recent NVDA versions.
* Updated translations.

### Version 1.11

* Updated compatibility flags for recent NVDA versions.
* Updated translations.
* Now, minimum supported version is 2022.4.

### Version 1.10

* Updated compatibility flags for recent NVDA versions.
* Updated translations.
* Updated documentation.
* Now, minimum supported version is 2021.3.
* The input will remain blocked after waking up from standby mode. Thanks to Javi Dominguez.

### Version 1.9

* Updated compatibility flags for recent NVDA versions.
* Updated translations.
* Updated documentation.

### Version 1.8

* Updated compatibility flags for recent NVDA versions.
* Updated translations.

### Version 1.7

* Updated compatibility flags for recent NVDA versions.
* Updated translations.

### Version 1.6

* Now, settings are removed only when the add-on is uninstalled. Configuration is nolonger reset when upgrading.
* New and updated translations.

### Version 1.5

* Added compatibility with recent NVDA releases.
* New translations.

### Version 1.4

* The addon gestures are unassigned by default.

### Version 1.3

* Added a configuration panel in settings dialog. For old NVDA versions, a menu item and a dialog have been added too.
* Added a setting to lock the mouse when NVDA is started.
* Added a setting to block also mouse clicks while mouse is locked.
* Small bugs fixed, some code optimizations and less duplicated strings for translators

### Version 1.2

* Now the mouse can also be locked
* New command to lock and unlock only the mouse

### Version 1.1

* If another addon has previously added a capture function to inputManager, it is restored when the input is unlocked.

### Version 1.0

* Initial release

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
