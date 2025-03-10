import cv2
import vlc
import ctypes
import numpy as np
import time

class VLCtoOpenCV:
    def __init__(self, rtsp_url):
        # Initialize VLC instance and media player
        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()
        self.media = self.instance.media_new(rtsp_url)
        self.media_player.set_media(self.media)

        # Set VLC to render video to a memory buffer
        opaque_data = {"message": "Hello from opaque data!"}
        opaque_ptr = ctypes.cast(ctypes.py_object(opaque_data), ctypes.c_void_p)
        self.media_player.video_set_callbacks(self.lock, self.unlock, self.display, opaque_ptr)
        self.media_player.video_set_format("RV32", 640, 480, 640 * 4) # Adjust width, height, and pitch as needed

        # Frame buffer for OpenCV
        self.frame = None
        self.locked = False

    def lock(self, opaque, planes):
        """Callback to lock the frame buffer."""
        if not self.locked:
            self.frame = np.zeros((480, 640, 4), dtype=np.uint8) # Adjust height and width as per your stream
            planes[0] = self.frame.ctypes.data
            self.locked = True

    def unlock(self, opaque, picture, planes):
        """Callback to unlock the frame buffer."""
        self.locked = False

    def display(self, opaque, picture):
        """Callback for when a frame is ready for display."""
        pass # No additional processing needed here for OpenCV integration

    def start(self):
        """Start the VLC media player."""
        self.media_player.play()
        time.sleep(1) # Give VLC time to start streaming

    def stop(self):
        """Stop the VLC media player."""
        self.media_player.stop()

    def get_frame(self):
        """Retrieve the current frame for OpenCV."""
        if self.frame is not None:
            return cv2.cvtColor(self.frame, cv2.COLOR_RGBA2BGR) # Convert RGBA to BGR for OpenCV
        return None


def main():
    rtsp_url = "rtsp://raf:rafraf@142.196.231.255?stream=1.sdp" # Replace with your RTSP URL
    vlc_stream = VLCtoOpenCV(rtsp_url)

    try:
        vlc_stream.start()

        while True:
            frame = vlc_stream.get_frame()
            if frame is not None:
                cv2.imshow("RTSP Stream", frame)

            # Break on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        vlc_stream.stop()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()