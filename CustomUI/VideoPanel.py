"""
Custom implementation of a WxPanel that will display a video from a given source
"""

import wx
import cv2
import numpy as np
import threading
import time
from datetime import datetime, timedelta
import calendar

class VideoPanel(wx.Panel):
    def __init__(self, parent, rtsp_url=0, camera_name="", savePath = "", videoDuration = 5, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.BORDER_THEME, name=wx.PanelNameStr):
        super().__init__(parent)

        self.capture_thread = None
        self.stop_event = threading.Event()
        self.rtsp_url = rtsp_url
        self.camera_name = camera_name
        self.save_path = savePath
        self.video_capture = None

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
        self.recording = True
        self.video_writer = None
        self.start_time = None
        self.duration = videoDuration #default Duration of the videos in minutes

        #People detection setup
        self.humanDetector = cv2.HOGDescriptor()
        self.humanDetector.setSVMDetector(cv2.HOGDescriptor.getDefaultPeopleDetector())

    def start_stream(self):
        if self.capture_thread is not None and self.capture_thread.is_alive():
            self.stop_stream()
        self.stop_event.clear()

        self.start_time = time.time()
        if self.recording:
            self.start_new_recording()

        self.capture_thread = threading.Thread(target=self.capture_frames)
        self.capture_thread.daemon = True
        self.capture_thread.start()
        print("Starting stream of: " + str(self.rtsp_url) +"\nOn Thread: " + self.capture_thread.name)
        self.timer.Start(1000 // 30)  # Refresh at 30 frames per second

    def start_new_recording(self):
        if self.video_writer:
            self.video_writer.release()
        if self.video_capture:
            video_width = int(self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
            video_height = int(self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
            video_fps = float(self.video_capture.get(cv2.CAP_PROP_FPS))
            print(f"Video Capture true: {video_width}, {video_height}, {video_fps}")
        else:
            video_width = 704
            video_height = 480
            video_fps = 6.0
        now = datetime.now()

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        time_interval = self.get_TimeInterval(now, self.duration)
        month_name = calendar.month_name[time_interval.month]
        date_string = f"{time_interval.year}{month_name}{time_interval.day}_{time_interval.hour}{time_interval.minute}"
        file_string = f"{self.save_path}\{self.camera_name}_{date_string}.mp4"
        print(f"Recording Video to: {file_string}")
        self.video_writer = cv2.VideoWriter(file_string, fourcc, video_fps, (video_width,video_height))
        if(self.video_writer.isOpened):
            print("Video Writer success")
        return
    
    def stop_stream(self):
        self.stop_event.set()
        if self.capture_thread is not None and self.capture_thread.is_alive():
            print("Stopping Thread: " + self.capture_thread.name)
            self.capture_thread.join() 
        self.timer.Stop()
        if self.video_writer:
            self.video_writer.release()

    def start_recording(self):
        self.recording = True
        self.start_new_recording()

    def stop_recording(self):
        self.recording = False

    def set_duration(self, duration):
        self.duration = duration

    def set_source(self, rtsp_url=0):
        self.rtsp_url = rtsp_url

    def set_name(self, name=""):
        self.camera_name = name

    def capture_frames(self):
        try:
            self.video_capture = cv2.VideoCapture(self.rtsp_url)
            while not self.stop_event.is_set():
                if(self.video_capture.isOpened()):
                    ret, frame = self.video_capture.read()
                    if ret:
                        self.error_text.Hide()
                        
                        #Detect people in image, returns bounding boxes for detected objects
                        boxes, weights = self.humanDetector.detectMultiScale(frame, winStride=(8,8))
                        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
                        for (xA, yA, xB, yB) in boxes:
                            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0) , 2)

                        self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        if self.recording:
                            current_time = time.time()
                            elapsed_time = current_time - self.start_time
                            if elapsed_time >= (self.duration * 60): #Time measured in seconds, multiple to minutes
                                self.start_new_recording()
                                self.start_time = current_time
                            if self.video_writer:
                                self.video_writer.write(frame)
                else:
                    print(f"Stream {self.rtsp_url} disconnected")
                    # try and fix the stream
                    self.video_capture.release()
                    self.video_capture = cv2.VideoCapture(self.rtsp_url)
            print(f"Ending Stream for {self.rtsp_url}")
            self.video_capture.release()
            self.Refresh()
        except Exception as e:
            print(f"Error in Stream {self.rtsp_url}\n{e}\n")
            self.error_text.Show()
            self.error_text.SetLabelText("Error in Camera\n" + str(self.rtsp_url))
            self.Refresh()

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

    def get_TimeInterval(self, start_time, duration):
        interval_start = start_time - timedelta(minutes=start_time.minute % duration)
        return interval_start