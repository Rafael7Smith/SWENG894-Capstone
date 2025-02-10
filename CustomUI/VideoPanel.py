"""
Custom implementation of a WxPanel that will display a video from a given source
"""
import wx
import cv2


class VideoPanel(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        super().__init__(parent)

        self.Bind(wx.EVT_TIMER, self.NextFrame)

        self.SetSource()
        self.SetFPS()
        self.StartStream()

    def SetSource(self, source=0):
        self.videoSource = cv2.VideoCapture(source)

    def SetFPS(self, fps=15):
        self.fps = fps

    def StartStream(self):
        self.timer = wx.Timer(self)
        self.timer.Start(milliseconds=int((1000 / self.fps)))

        ret, video = self.videoSource.read()

        if ret: 
            video = cv2.flip(video, 1)
            video = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
            
            self.bmp = wx.Bitmap.FromBuffer(self.GetSize().GetWidth(),self.GetSize().GetHeight(), video)
 

    def StopStream(self):
        self.timer.Stop()

    def NextFrame(self, event):
        ret, video = self.videoSource.read()
        if ret:
            video = cv2.flip(video, 1)
            video = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
            self.bmp.CopyFromBuffer(video)
            self.Refresh()