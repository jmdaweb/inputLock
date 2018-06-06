# Input Lock
Version 1.3

## Introduction

Do you have kids or pets at home? Do you have a cat and It likes very much climbing your table and walking over your keyboard? Do you accidentally move the mouse to random parts in the screen while using your laptop? Then Input Lock is for you! You will be able to leave your computer alone and turned on without risk.

Once installed, you will be able to lock your keyboard, touch screen, if your laptop has one, mouse and Braille display.

## Usage

This addon adds an extra gesture to NVDA. By default it's NVDA+k, but it can (and should) be changed from Input gestures dialog. Read the NVDA User Guide for more information.

When you press that gesture, NVDA will say "Input locked". Your input devices will be blocked until you press the same gesture again. In that moment, NVDA will say "Input unlocked" and everything will work as usual.

If you press NVDA+shift+m, your mouse will be locked. Press this command again to unlock it. Of course, you can customize it from Input Gestures dialog. While mouse is locked, you can use NVDA gestures to move it, and click with left and right buttons, but You can't move the mouse itself. Mouse clicks can also be disabled from Input lock category in NVDA settings dialog (NVDA 2018.2 and later) or from add-on settings dialog for older versions, available under preferences menu. In addition, from these settings you can control wether mouse locks when NVDA is started or not.

Note: when mouse clicks are blocked, you can't use any NVDA gestures to work with the mouse.

## Limitations

Input Lock has the following limitations:

* The shortcut control+alt+del can be used even when the keyboard is locked.

## Contact info

This addon has been developed by Jose Manuel Delicado. If you want to contact me, send an e-mail to jm.delicado@nvda.es, or open an issue on GitHub at https://github.com/jmdaweb/enhancedAria

## Changelog

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

