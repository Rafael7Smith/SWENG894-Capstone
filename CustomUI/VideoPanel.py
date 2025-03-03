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

        # Create a wx.Timer to refresh the panel periodically
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_frame, self.timer)
        self.frame = None
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def start_stream(self):
        if self.capture_thread is not None and self.capture_thread.is_alive():
            self.stop_stream()

        self.stop_event.clear()
        self.capture_thread = threading.Thread(target=self.capture_frames)
        self.capture_thread.daemon = True
        self.capture_thread.start()
        self.timer.Start(1000 // 30)  # Refresh at 30 frames per second

    def stop_stream(self):
        self.stop_event.set()
        if self.capture_thread is not None:
            self.capture_thread.join()
        self.timer.Stop()

    def change_source(self, rtsp_url=0):
        self.rtsp_url = rtsp_url
        self.start_stream()

    def capture_frames(self):
        cap = cv2.VideoCapture(self.rtsp_url)
        
        while not self.stop_event.is_set():
            ret, frame = cap.read()
            if ret:
                self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.Refresh()
            else:
                break
        cap.release()

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