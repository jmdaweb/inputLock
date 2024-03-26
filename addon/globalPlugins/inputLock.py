# Input Lock addon for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2022 Jose Manuel Delicado <jm.delicado@nvda.es>
import globalPluginHandler
import globalCommands
import addonHandler
import ui
import inputCore
import mouseHandler
import winInputHook
import winreg
import winUser
import config
from gui import guiHelper
from keyboardHandler import KeyboardInputGesture
import wx
import versionInfo
from gui import NVDASettingsDialog
from gui.settingsDialogs import SettingsPanel
from scriptHandler import script
addonHandler.initTranslation()
speakOnDemand = {"speakOnDemand": True} if versionInfo.version_year >= 2024 else {}

confspec = {
	"blockMouseAtStartup": "boolean(default=false)",
	"blockClicks": "boolean(default=false)"
}
config.conf.spec['inputlock'] = confspec

allowedMouseActions = [
	mouseHandler.WM_LBUTTONDOWN,
	mouseHandler.WM_LBUTTONUP,
	mouseHandler.WM_RBUTTONDOWN,
	mouseHandler.WM_RBUTTONUP]
mouseCallbackFunc = None

def getTouchpadStatus():
	"""
	Returns the status of the Precision Touchpad.

	Returns:
		bool: True if the touchpad is enabled, False if disabled.
		None: If there's an error accessing the registry.
	"""
	try:
		with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\PrecisionTouchPad\Status") as key:
			return bool(winreg.QueryValueEx(key, "Enabled")[0])
	except FileNotFoundError:
		return None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.locked = False
		self.prevCaptureFunc = None
		self.cursorPos = None
		self.gesture = None
		self.mouseLocked = False
		if config.conf['inputlock']['blockMouseAtStartup']:
			self.script_mouseLock(None)
		NVDASettingsDialog.categoryClasses.append(inputLockPanel)

	def terminate(self):
		if self.mouseLocked:
			# We assume that this plugin won't terminate if all input is locked,
			# but in case of mouse, we must release it
			self.script_mouseLock(None)
		try:
			NVDASettingsDialog.categoryClasses.remove(inputLockPanel)
		except RuntimeError:
			pass

	def mouseCapture(self, msg, x, y, injected):
		if msg in allowedMouseActions and not self.locked and\
		not config.conf['inputlock']['blockClicks']:
			return mouseCallbackFunc(msg, x, y, injected)
		else:
			if self.mouseLocked and not self.locked:
				mouseHandler.executeMouseMoveEvent(self.cursorPos[0], self.cursorPos[1])
			winUser.setCursorPos(self.cursorPos[0], self.cursorPos[1])

	def capture(self, gesture):
		if not self.gesture or gesture.displayName == self.gesture.displayName:
			return True
		else:
			return False

	def lockMouse(self):
		global mouseCallbackFunc
		mouseCallbackFunc = winInputHook.mouseCallback
		winInputHook.setCallbacks(mouse=self.mouseCapture)
		self.cursorPos = winUser.getCursorPos()

	def unlockMouse(self):
		global mouseCallbackFunc
		winInputHook.setCallbacks(mouse=mouseCallbackFunc)
		self.cursorPos = None
		mouseCallbackFunc = None

	def event_foreground(self, obj, next):
		try:
			window = obj.appModule.productName
		except Exception:
			window = ""
		if self.locked and window != 'Microsoft.LockApp':
			self.prevCaptureFunc = inputCore.manager._captureFunc
			inputCore.manager._captureFunc = self.capture
		next()

	@script(
		# TRANSLATORS: gesture description for Input gestures dialog
		description=_("Toggle input lock"),
		category=globalCommands.SCRCAT_INPUT,
		**speakOnDemand)
	def script_inputLock(self, gesture):
		self.locked = not self.locked
		self.gesture = gesture
		if self.locked:
			# TRANSLATORS: message spoken when the input is locked
			ui.message(_("Input locked"))
			self.prevCaptureFunc = inputCore.manager._captureFunc
			inputCore.manager._captureFunc = self.capture
			if not self.mouseLocked:
				self.lockMouse()
		else:
			# TRANSLATORS: message spoken when the input is unlocked
			ui.message(_("Input unlocked"))
			inputCore.manager._captureFunc = self.prevCaptureFunc
			if not self.mouseLocked:
				self.unlockMouse()
			self.gesture = None
			self.prevCaptureFunc = None

	@script(
		# TRANSLATORS: gesture description for Input gestures dialog
		description=_("Toggle mouse lock"),
		category=globalCommands.SCRCAT_INPUT,
		**speakOnDemand)
	def script_mouseLock(self, gesture):
		self.mouseLocked = not self.mouseLocked
		if self.mouseLocked:
			# TRANSLATORS: message spoken when the mouse is locked
			ui.message(_("Mouse locked"))
			self.lockMouse()
		else:
			# TRANSLATORS: message spoken when the mouse is unlocked
			ui.message(_("Mouse unlocked"))
			self.unlockMouse()

	@script(
		# TRANSLATORS: gesture description for Input gestures dialog
		description=_("Toggle touchpad lock"),
		category=globalCommands.SCRCAT_INPUT,
		**speakOnDemand)
	def script_SwitchTouchpad(self, gesture):
		if getTouchpadStatus() is None:
			return ui.message(_("not support"))
		KeyboardInputGesture.fromName("windows+control+f24").send()
		ui.message(_("Touchpad unlocked") if getTouchpadStatus() else _("Touchpad locked"))


class inputLockPanel(SettingsPanel):
	# TRANSLATORS: Settings dialog and/or panel title
	title = _("Input lock settings")

	def makeSettings(self, sizer):
		helper = guiHelper.BoxSizerHelper(self, sizer=sizer)
		self.blockmouseenabled = helper.addItem(wx.CheckBox(
			# TRANSLATORS: block mouse at startup checkbox
			self, wx.ID_ANY, label=_("Block mouse when NVDA is started")))
		self.blockmouseenabled.SetValue(
			config.conf['inputlock']['blockMouseAtStartup'])
		self.blockclicksenabled = helper.addItem(wx.CheckBox(
			# TRANSLATORS: block also mouse clicks checkbox
			self, wx.ID_ANY, label=_("Block clicks when mouse is locked")))
		self.blockclicksenabled.SetValue(config.conf['inputlock']['blockClicks'])

	def onSave(self):
		config.conf['inputlock']['blockMouseAtStartup'] = \
		self.blockmouseenabled.GetValue()
		config.conf['inputlock']['blockClicks'] = self.blockclicksenabled.GetValue()
