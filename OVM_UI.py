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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Open Vision Managment", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar = wx.MenuBar( 0 )
		self.File = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.File, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.File, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.Append( self.m_menuItem2 )

		self.File.AppendSeparator()

		self.m_menuItem3 = wx.MenuItem( self.File, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.Append( self.m_menuItem3 )

		self.m_menubar.Append( self.File, u"File" )

		self.SetMenuBar( self.m_menubar )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = VideoPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.Hide()

		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


