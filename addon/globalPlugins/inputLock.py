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
import config
import gui
from gui import settingsDialogs
try:
	from gui import NVDASettingsDialog
	from gui.settingsDialogs import SettingsPanel
except:
	SettingsPanel=object # give the panel class something it can inherit from
import wx

#TRANSLATORS: Settings dialog and/or panel title
addonSettingsTitle=_("Input lock settings")

confspec={
	"blockMouseAtStartup":"boolean(default=false)",
	"blockClicks":"boolean(default=false)"
}
config.conf.spec['inputlock']=confspec

allowedMouseActions=[mouseHandler.WM_LBUTTONDOWN, mouseHandler.WM_LBUTTONUP, mouseHandler.WM_RBUTTONDOWN, mouseHandler.WM_RBUTTONUP]
mouseCallbackFunc=None

# Common functions for dialog and panel classes to create and retrieve settings
def createSettings(obj, sizer):
	#TRANSLATORS: block mouse at startup checkbox
	obj.blockmouseenabled=wx.CheckBox(obj, wx.NewId(), label=_("Block mouse when NVDA is started"))
	obj.blockmouseenabled.SetValue(config.conf['inputlock']['blockMouseAtStartup'])
	sizer.Add(obj.blockmouseenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: block also mouse clicks checkbox
	obj.blockclicksenabled=wx.CheckBox(obj, wx.NewId(), label=_("Block clicks when mouse is locked"))
	obj.blockclicksenabled.SetValue(config.conf['inputlock']['blockClicks'])
	sizer.Add(obj.blockclicksenabled,border=10,flag=wx.BOTTOM)

def storeSettings(obj):
	config.conf['inputlock']['blockMouseAtStartup']=obj.blockmouseenabled.GetValue()
	config.conf['inputlock']['blockClicks']=obj.blockclicksenabled.GetValue()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = globalCommands.SCRCAT_INPUT
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.locked=False
		self.prevCaptureFunc=None
		self.cursorPos=None
		self.gesture=None
		self.mouseLocked=False
		if config.conf['inputlock']['blockMouseAtStartup']:
			self.script_mouseLock(None)
		if hasattr(settingsDialogs, 'SettingsPanel'):
			NVDASettingsDialog.categoryClasses.append(inputLockPanel)
		else:
			self.prefsMenu = gui.mainFrame.sysTrayIcon.menu.GetMenuItems()[0].GetSubMenu()
			#TRANSLATORS: The configuration option in NVDA Preferences menu
			self.inputLockSettingsItem = self.prefsMenu.Append(wx.ID_ANY, _("Input lock settings..."), _("Change input lock settings"))
			gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onInputLockMenu, self.inputLockSettingsItem)

	def terminate(self):
		if self.mouseLocked:
			# We assume that this plugin won't terminate if all input is locked, but in case of mouse, we must release it
			self.script_mouseLock(None)
		try:
			if hasattr(settingsDialogs, 'SettingsPanel'):
				NVDASettingsDialog.categoryClasses.remove(inputLockPanel)
			else:
				self.prefsMenu.RemoveItem(self.inputLockSettingsItem)
		except:
			pass

	def onInputLockMenu(self, evt):
		gui.mainFrame._popupSettingsDialog(inputLockSettings)

	def mouseCapture(self, msg, x, y, injected):
		if msg in allowedMouseActions and not self.locked and not config.conf['inputlock']['blockClicks']:
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
		global mouseCallbackFunc
		winInputHook.setCallbacks(mouse=mouseCallbackFunc)
		self.cursorPos=None
		mouseCallbackFunc=None

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

class inputLockSettings(settingsDialogs.SettingsDialog):
	title=addonSettingsTitle

	def makeSettings(self, sizer):
		createSettings(self, sizer)

	def postInit(self):
		self.blockmouseenabled.SetFocus()

	def onOk(self, evt):
		storeSettings(self)
		super(inputLockSettings, self).onOk(evt)

class inputLockPanel(SettingsPanel):
	title=addonSettingsTitle

	def makeSettings(self, sizer):
		createSettings(self, sizer)

	def onSave(self):
		storeSettings(self)
