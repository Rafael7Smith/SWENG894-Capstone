# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class OVM_Frame
###########################################################################

class OVM_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Open Vision Managment", pos = wx.DefaultPosition, size = wx.Size( 931,607 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.OVM_MenuBar = wx.MenuBar( 0 )
		self.File = wx.Menu()
		self.FileMenuItem_Video = wx.MenuItem( self.File, wx.ID_ANY, u"Video Screen", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.Append( self.FileMenuItem_Video )

		self.FileMenuItem_Settings = wx.MenuItem( self.File, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.Append( self.FileMenuItem_Settings )

		self.File.AppendSeparator()

		self.FileMenuItem_Exit = wx.MenuItem( self.File, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.Append( self.FileMenuItem_Exit )

		self.OVM_MenuBar.Append( self.File, u"File" )

		self.SetMenuBar( self.OVM_MenuBar )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.panel_mainvideo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL, u"panel_mainvideo" )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.panel_mainvideo, wx.ID_ANY, u"Available Cameras" ), wx.VERTICAL )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Number of feeds", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer32.Add( self.m_staticText22, 0, wx.ALIGN_CENTER, 5 )

		self.Video_NumFeeds_Sldr = wx.Slider( sbSizer1.GetStaticBox(), wx.ID_ANY, 6, 1, 8, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
		bSizer32.Add( self.Video_NumFeeds_Sldr, 0, wx.ALIGN_CENTER, 5 )


		sbSizer1.Add( bSizer32, 0, wx.EXPAND, 5 )

		Video_AvailCams_chkLstChoices = [u"Cam 1", u"Cam 2", u"Cam 3", u"Cam 4", u"Cam 5", u"Cam 6", u"Cam 7", u"Cam 8"]
		self.Video_AvailCams_chkLst = wx.CheckListBox( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Video_AvailCams_chkLstChoices, 0 )
		sbSizer1.Add( self.Video_AvailCams_chkLst, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )

		self.gridsizer_videofeeds = wx.GridSizer( 0, 2, 0, 0 )


		bSizer3.Add( self.gridsizer_videofeeds, 3, wx.EXPAND, 5 )


		self.panel_mainvideo.SetSizer( bSizer3 )
		self.panel_mainvideo.Layout()
		bSizer3.Fit( self.panel_mainvideo )
		bSizer1.Add( self.panel_mainvideo, 1, wx.EXPAND |wx.ALL, 5 )

		self.panel_mainsettings = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.staticText_SettingsTitle = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Settings Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_SettingsTitle.Wrap( -1 )

		bSizer2.Add( self.staticText_SettingsTitle, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Manage Cameras", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer13.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText20 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Camera Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer30.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.Settings_CamName_txtCtrl = wx.TextCtrl( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.Settings_CamName_txtCtrl, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer30, 1, wx.EXPAND, 5 )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Camera Ip Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer29.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.Settings_CamAddr_txtCtrl = wx.TextCtrl( self.panel_mainsettings, wx.ID_ANY, u"IP Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.Settings_CamAddr_txtCtrl, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer29, 1, wx.EXPAND, 5 )


		bSizer27.Add( bSizer31, 1, wx.EXPAND, 5 )

		self.Settings_AddCam_btn = wx.Button( self.panel_mainsettings, wx.ID_ANY, u"Add new Camera", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.Settings_AddCam_btn, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer27, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.panel_mainsettings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer26.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		Settings_CamList_chkLstChoices = [u"Cam 1", u"Cam 2", u"Cam 3"]
		self.Settings_CamList_chkLst = wx.CheckListBox( self.panel_mainsettings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Settings_CamList_chkLstChoices, 0 )
		bSizer28.Add( self.Settings_CamList_chkLst, 0, wx.ALL, 5 )

		self.Settings_DelCam_btn = wx.Button( self.panel_mainsettings, wx.ID_ANY, u"Remove Camera", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.Settings_DelCam_btn, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer28, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer26, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Storage Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer15.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Enable Video Saving", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer18.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.Settings_EnableSave_chkBox = wx.CheckBox( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.Settings_EnableSave_chkBox, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer17.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.Settings_SaveLoc_dirPck = wx.DirPickerCtrl( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer17.Add( self.Settings_SaveLoc_dirPck, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Storage Size (GB)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer19.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.Settings_StorageSize_txtCtrl = wx.TextCtrl( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.Settings_StorageSize_txtCtrl, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer19, 0, wx.EXPAND, 5 )

		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText161 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"File Size (Minutes)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		bSizer191.Add( self.m_staticText161, 0, wx.ALL, 5 )

		self.Settings_FileSize_txtCtrl = wx.TextCtrl( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.Settings_FileSize_txtCtrl, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer191, 0, wx.EXPAND, 5 )

		self.Settings_SaveSettings_btn = wx.Button( self.panel_mainsettings, wx.ID_ANY, u"Save Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.Settings_SaveSettings_btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer15.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer15, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer12, 1, wx.EXPAND, 5 )


		self.panel_mainsettings.SetSizer( bSizer2 )
		self.panel_mainsettings.Layout()
		bSizer2.Fit( self.panel_mainsettings )
		bSizer1.Add( self.panel_mainsettings, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Handle_App_Close )
		self.Bind( wx.EVT_MENU, self.Handle_MenuItem_Video, id = self.FileMenuItem_Video.GetId() )
		self.Bind( wx.EVT_MENU, self.Handle_MenuItem_Settings, id = self.FileMenuItem_Settings.GetId() )
		self.Bind( wx.EVT_MENU, self.Handle_MenuItem_Exit, id = self.FileMenuItem_Exit.GetId() )
		self.Video_NumFeeds_Sldr.Bind( wx.EVT_SCROLL_CHANGED, self.Handle_Video_NumFeeds )
		self.Video_AvailCams_chkLst.Bind( wx.EVT_CHECKLISTBOX, self.Handle_CameraChkLst_Toggle )
		self.Settings_AddCam_btn.Bind( wx.EVT_BUTTON, self.Handle_Setting_NewCameraBtn )
		self.Settings_DelCam_btn.Bind( wx.EVT_BUTTON, self.Handle_Setting_RemoveCameraBtn )
		self.Settings_EnableSave_chkBox.Bind( wx.EVT_CHECKBOX, self.Handle_Setting_EnDisSaving )
		self.Settings_SaveLoc_dirPck.Bind( wx.EVT_DIRPICKER_CHANGED, self.Handle_Setting_SaveLocation )
		self.Settings_SaveSettings_btn.Bind( wx.EVT_BUTTON, self.Handle_Setting_SaveSettings )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Handle_App_Close( self, event ):
		event.Skip()

	def Handle_MenuItem_Video( self, event ):
		event.Skip()

	def Handle_MenuItem_Settings( self, event ):
		event.Skip()

	def Handle_MenuItem_Exit( self, event ):
		event.Skip()

	def Handle_Video_NumFeeds( self, event ):
		event.Skip()

	def Handle_CameraChkLst_Toggle( self, event ):
		event.Skip()

	def Handle_Setting_NewCameraBtn( self, event ):
		event.Skip()

	def Handle_Setting_RemoveCameraBtn( self, event ):
		event.Skip()

	def Handle_Setting_EnDisSaving( self, event ):
		event.Skip()

	def Handle_Setting_SaveLocation( self, event ):
		event.Skip()

	def Handle_Setting_SaveSettings( self, event ):
		event.Skip()


