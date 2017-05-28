#Input Lock addon for NVDA
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2017 Jose Manuel Delicado <jmdaweb@hotmail.com>
import globalPluginHandler
import addonHandler
addonHandler.initTranslation()
import ui
import inputCore

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# TRANSLATORS: category name shown in the Input gestures dialog.
	scriptCategory = _("Input")
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.locked=False
		self.prevCaptureFunc=None

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
		else:
			# TRANSLATORS: message spoken when the input is unlocked
			ui.message(_("input unlocked"))
			inputCore.manager._captureFunc=self.prevCaptureFunc

	# TRANSLATORS: gesture description for Input gestures dialog
	script_inputLock.__doc__=_("Toggle input lock")

	__gestures={
		"kb:NVDA+k": "inputLock",
	}
