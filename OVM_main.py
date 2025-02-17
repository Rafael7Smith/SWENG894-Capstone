"""
Open Vision Management, Main file
Starts up the WxPython app
"""

import wx
import OVM_UI_Adapater

print(f"Open Vision Management Startup")

app = wx.App()

frame = OVM_UI_Adapater.OVM_UI_Adapater(None)

frame.Show()

app.MainLoop()