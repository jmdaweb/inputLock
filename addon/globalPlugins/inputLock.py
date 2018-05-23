#Input Lock addon for NVDA
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Jose Manuel Delicado <jmdaweb@hotmail.com>
import globalPluginHandler
import addonHandler
addonHandler.initTranslation()
import ui
import inputCore
import mouseHandler
import winInputHook
import winUser

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# TRANSLATORS: category name shown in the Input gestures dialog.
	scriptCategory = _("Input")
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.locked=False
		self.prevCaptureFunc=None
		self.mouseCallbackFunc=None
		self.cursorPos=None
		self.gesture=None

	def mouseCapture(self, msg, x, y, injected):
		winUser.setCursorPos(self.cursorPos[0], self.cursorPos[1])

	def capture(self, gesture):
		if gesture.displayName==self.gesture.displayName:
			return True
		else:
			return False

	def script_inputLock(self, gesture):
		self.locked=not self.locked
		self.gesture=gesture
		if self.locked:
			# TRANSLATORS: message spoken when the input is locked
			ui.message(_("input locked"))
			self.prevCaptureFunc=inputCore.manager._captureFunc
			inputCore.manager._captureFunc=self.capture
			self.mouseCallbackFunc=winInputHook.mouseCallback
			winInputHook.setCallbacks(mouse=self.mouseCapture)
			self.cursorPos=winUser.getCursorPos()
		else:
			# TRANSLATORS: message spoken when the input is unlocked
			ui.message(_("input unlocked"))
			inputCore.manager._captureFunc=self.prevCaptureFunc
			winInputHook.setCallbacks(mouse=self.mouseCallbackFunc)
			self.cursorPos=None
			self.gesture=None
	# TRANSLATORS: gesture description for Input gestures dialog
	script_inputLock.__doc__=_("Toggle input lock")

	__gestures={
		"kb:NVDA+k": "inputLock",
	}
