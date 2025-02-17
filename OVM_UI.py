# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from CustomUI.VideoPanel import VideoPanel
import wx
import wx.xrc

###########################################################################
## Class OVM_Frame
###########################################################################

class OVM_Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Open Vision Managment", pos = wx.DefaultPosition, size = wx.Size( 799,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

		self.panel_mainvideo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_mainvideo.Hide()

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.panel_mainvideo, wx.ID_ANY, u"Available Cameras" ), wx.VERTICAL )

		m_checkList1Choices = [u"Cam 1", u"Cam 2", u"Cam 3"]
		self.m_checkList1 = wx.CheckListBox( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
		sbSizer1.Add( self.m_checkList1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_panel4 = VideoPanel( self.panel_mainvideo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Cam 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer5.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer5 )
		self.m_panel4.Layout()
		bSizer5.Fit( self.m_panel4 )
		gSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel41 = wx.Panel( self.panel_mainvideo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText61 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"Cam 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		bSizer51.Add( self.m_staticText61, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel41.SetSizer( bSizer51 )
		self.m_panel41.Layout()
		bSizer51.Fit( self.m_panel41 )
		gSizer1.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel43 = wx.Panel( self.panel_mainvideo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer53 = wx.BoxSizer( wx.VERTICAL )


		bSizer53.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText63 = wx.StaticText( self.m_panel43, wx.ID_ANY, u"Cam 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )

		bSizer53.Add( self.m_staticText63, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer53.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel43.SetSizer( bSizer53 )
		self.m_panel43.Layout()
		bSizer53.Fit( self.m_panel43 )
		gSizer1.Add( self.m_panel43, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel42 = wx.Panel( self.panel_mainvideo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer52 = wx.BoxSizer( wx.VERTICAL )


		bSizer52.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText62 = wx.StaticText( self.m_panel42, wx.ID_ANY, u"Cam 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		bSizer52.Add( self.m_staticText62, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer52.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel42.SetSizer( bSizer52 )
		self.m_panel42.Layout()
		bSizer52.Fit( self.m_panel42 )
		gSizer1.Add( self.m_panel42, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel44 = wx.Panel( self.panel_mainvideo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer54 = wx.BoxSizer( wx.VERTICAL )


		bSizer54.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText64 = wx.StaticText( self.m_panel44, wx.ID_ANY, u"Cam 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		bSizer54.Add( self.m_staticText64, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer54.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel44.SetSizer( bSizer54 )
		self.m_panel44.Layout()
		bSizer54.Fit( self.m_panel44 )
		gSizer1.Add( self.m_panel44, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( gSizer1, 3, wx.EXPAND, 5 )


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

		self.m_textCtrl5 = wx.TextCtrl( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_textCtrl5, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer30, 1, wx.EXPAND, 5 )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Camera Ip Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer29.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.panel_mainsettings, wx.ID_ANY, u"IP Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_textCtrl4, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer29, 1, wx.EXPAND, 5 )


		bSizer27.Add( bSizer31, 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self.panel_mainsettings, wx.ID_ANY, u"Add new Camera", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_button1, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer27, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.panel_mainsettings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer26.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		m_checkList2Choices = [u"Cam 1", u"Cam 2", u"Cam 3"]
		self.m_checkList2 = wx.CheckListBox( self.panel_mainsettings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList2Choices, 0 )
		bSizer28.Add( self.m_checkList2, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.panel_mainsettings, wx.ID_ANY, u"Remove Camera", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button2, 0, wx.ALL, 5 )


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

		self.m_checkBox1 = wx.CheckBox( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_checkBox1, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer17.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer17.Add( self.m_dirPicker1, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"Storage Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer19.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer19, 0, wx.EXPAND, 5 )

		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText161 = wx.StaticText( self.panel_mainsettings, wx.ID_ANY, u"File Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		bSizer191.Add( self.m_staticText161, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.panel_mainsettings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.m_textCtrl3, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer191, 0, wx.EXPAND, 5 )


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
		self.Bind( wx.EVT_MENU, self.Handle_MenuItem_Video, id = self.FileMenuItem_Video.GetId() )
		self.Bind( wx.EVT_MENU, self.Handle_MenuItem_Settings, id = self.FileMenuItem_Settings.GetId() )
		self.Bind( wx.EVT_MENU, self.Handle_MenuItem_Exit, id = self.FileMenuItem_Exit.GetId() )
		self.m_checkList1.Bind( wx.EVT_CHECKLISTBOX, self.Handle_CameraChkLst_Toggle )
		self.m_button1.Bind( wx.EVT_BUTTON, self.Handle_Setting_NewCameraBtn )
		self.m_button2.Bind( wx.EVT_BUTTON, self.Handle_Setting_RemoveCameraBtn )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.Handle_Setting_EnDisSaving )
		self.m_dirPicker1.Bind( wx.EVT_DIRPICKER_CHANGED, self.Handle_Setting_SaveLocation )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Handle_MenuItem_Video( self, event ):
		event.Skip()

	def Handle_MenuItem_Settings( self, event ):
		event.Skip()

	def Handle_MenuItem_Exit( self, event ):
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


