"""
Open Vision Management, Main file
Starts up the WxPython app
"""

import wx


print(f"Open Vision Management Startup")

app = wx.App()

import pkg_resources
#Ensure library versions are correct
try:
    # pkg_resources.require("opencv-python==4.10.0.84")
    # pkg_resources.require("numpy==2.0.0")
    import OVM_UI_Adapater
    frame = OVM_UI_Adapater.OVM_UI_Adapater(None)

    frame.Show()

    app.MainLoop()
except Exception as e:
	wx.MessageBox("""This application requires specific versions of OpenCV and Numpy to function.\n
	Please run the following commands to uninstall these libraries and install the correct versions:\n
	pip uninstall opencv-python\n
	pip uninstall numpy\n
	pip install opencv-python==4.10.0.84\n
	pip install numpy==2.0.0\n
    Error message:\n
	""" + str(e))