"""
Custom implementation of a WxPanel that will display a video from a given source
"""

import wx
import cv2
import threading


class VideoPanel(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.BORDER_THEME, name=wx.PanelNameStr):
        super().__init__(parent)

        self.capture_thread = None
        self.stop_event = threading.Event()
        self.rtsp_url = 0

        # Default to Error with video stream
        self.error_text = wx.StaticText(self, wx.ID_ANY, u"Error with Camera", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.error_sizer = wx.BoxSizer(wx.VERTICAL)
        self.error_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        self.error_sizer.Add(self.error_text, 1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.error_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        self.SetSizer(self.error_sizer)
        self.error_text.Hide()
        
        # Create a wx.Timer to refresh the panel periodically
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_frame, self.timer)
        self.frame = None
        self.Bind(wx.EVT_PAINT, self.on_paint)

        #Recording Video Function
        self.recording = False
        self.video_writer = None
        self.start_time = None
        self.duration = 0

    def start_stream(self):
        
        if self.capture_thread is not None and self.capture_thread.is_alive():
            self.stop_stream()

        self.stop_event.clear()
        self.capture_thread = threading.Thread(target=self.capture_frames)
        self.capture_thread.daemon = True
        self.capture_thread.start()
        print("Starting stream of: " + str(self.rtsp_url) +"\nOn Thread: " + self.capture_thread.name)
        self.timer.Start(1000 // 30)  # Refresh at 30 frames per second

    def stop_stream(self):
        self.stop_event.set()
        if self.capture_thread is not None and self.capture_thread.is_alive():
            print("Stopping Thread: " + self.capture_thread.name)
            self.capture_thread.join() 
        self.timer.Stop()

    def set_source(self, rtsp_url=0):
        self.rtsp_url = rtsp_url

    def capture_frames(self):
        try:
            cap = cv2.VideoCapture(self.rtsp_url)
            while not self.stop_event.is_set():
                if(cap.isOpened()):
                    ret, frame = cap.read()
                    if ret:
                        self.error_text.Hide()
                        self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                else:
                    print(f"Stream {self.rtsp_url} disconnected")
                    # try and fix the stream
                    cap.release()
                    cap = cv2.VideoCapture(self.rtsp_url)
                    #break
        except Exception as e:
            print(f"Error in Stream {self.rtsp_url}\n{e}\n")

    def update_frame(self, event):
        self.Refresh()

    def on_paint(self, event):
        if self.frame is not None:
            panel_size = self.GetSize()
            resized_frame = cv2.resize(self.frame, (panel_size.width, panel_size.height))
            height, width = resized_frame.shape[:2]
            bitmap = wx.Bitmap.FromBuffer(width, height, resized_frame)
            dc = wx.BufferedPaintDC(self)
            dc.DrawBitmap(bitmap, 0, 0)