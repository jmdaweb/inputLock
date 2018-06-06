#Input Lock addon for NVDA
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Jose Manuel Delicado <jmdaweb@hotmail.com>
import globalPluginHandler
import globalCommands
import addonHandler
addonHandler.initTranslation()
import ui
import inputCore
import mouseHandler
import winInputHook
import winUser

allowedMouseActions=[mouseHandler.WM_LBUTTONDOWN, mouseHandler.WM_LBUTTONUP, mouseHandler.WM_RBUTTONDOWN, mouseHandler.WM_RBUTTONUP]
mouseCallbackFunc=None
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = globalCommands.SCRCAT_INPUT
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.locked=False
		self.prevCaptureFunc=None
		self.cursorPos=None
		self.gesture=None
		self.mouseLocked=False

	def mouseCapture(self, msg, x, y, injected):
		if msg in allowedMouseActions and not self.locked:
			return mouseCallbackFunc(msg, x, y, injected)
		else:
			if self.mouseLocked and not self.locked:
				mouseHandler.executeMouseMoveEvent(self.cursorPos[0], self.cursorPos[1])
			winUser.setCursorPos(self.cursorPos[0], self.cursorPos[1])

	def capture(self, gesture):
		if gesture.displayName==self.gesture.displayName:
			return True
		else:
			return False

	def lockMouse(self):
		global mouseCallbackFunc
		mouseCallbackFunc=winInputHook.mouseCallback
		winInputHook.setCallbacks(mouse=self.mouseCapture)
		self.cursorPos=winUser.getCursorPos()

	def unlockMouse(self):
		winInputHook.setCallbacks(mouse=mouseCallbackFunc)
		self.cursorPos=None
		self.mouseCallbackFunc=None

	def script_inputLock(self, gesture):
		self.locked=not self.locked
		self.gesture=gesture
		if self.locked:
			# TRANSLATORS: message spoken when the input is locked
			ui.message(_("Input locked"))
			self.prevCaptureFunc=inputCore.manager._captureFunc
			inputCore.manager._captureFunc=self.capture
			if not self.mouseLocked:
				self.lockMouse()
		else:
			# TRANSLATORS: message spoken when the input is unlocked
			ui.message(_("Input unlocked"))
			inputCore.manager._captureFunc=self.prevCaptureFunc
			if not self.mouseLocked:
				self.unlockMouse()
			self.gesture=None
			self.prevCaptureFunc=None
	# TRANSLATORS: gesture description for Input gestures dialog
	script_inputLock.__doc__=_("Toggle input lock")

	def script_mouseLock(self, gesture):
		self.mouseLocked=not self.mouseLocked
		if self.mouseLocked:
			# TRANSLATORS: message spoken when the mouse is locked
			ui.message(_("Mouse locked"))
			self.lockMouse()
		else:
			# TRANSLATORS: message spoken when the mouse is unlocked
			ui.message(_("Mouse unlocked"))
			self.unlockMouse()
	# TRANSLATORS: gesture description for Input gestures dialog
	script_mouseLock.__doc__=_("Toggle mouse lock")

	__gestures={
		"kb:NVDA+k": "inputLock",
		"kb:NVDA+shift+m": "mouseLock"
	}
