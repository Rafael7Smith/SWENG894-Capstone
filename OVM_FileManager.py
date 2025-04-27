import os
import time
import threading

class OVM_FileManager:
    def __init__(self, directory, duration, max_size):
        self.directory = directory
        self.duration = duration
        self.max_size = max_size

    def get_directory_size(self):
        #Calculate the total size of the '.mp4' files in the directory.
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(self.directory):
            for filename in filenames:
                if filename.endswith('.mp4'):
                    file_path = os.path.join(dirpath, filename)
                    if os.path.isfile(file_path):
                        total_size += os.path.getsize(file_path)
        # Convert total_size from bytes to GigaBytes
        # 1 GB = 1024 MB = 1,048,576 KB = 1,073,741,824 Bytes (2^30)
        total_size_gb = total_size / 1073741824
        return total_size_gb

    def delete_oldest_mp4(self):
        #Delete the oldest '.mp4' file in the directory.
        
        mp4_files = [f for f in os.listdir(self.directory) if f.endswith('.mp4')]
        if not mp4_files:
            return
        
        # There must be at least one file
        if len(mp4_files) <=1:
            return
        
        oldest_file = min(mp4_files, key=lambda f: os.path.getctime(os.path.join(self.directory, f)))
        os.remove(os.path.join(self.directory, oldest_file))
        print(f"Deleted: {oldest_file}")

    def monitor_directory(self):
        #Monitor the directory and ensure it does not exceed the maximum size.
        while True:
            current_size = self.get_directory_size()
            if current_size > self.max_size:
                self.delete_oldest_mp4()
            time.sleep(self.duration * 60) #Given duration is in minutes

    def start_monitoring(self):
        print(f"Monitoring started. Directory: {self.directory} | Max Size: {self.max_size} GB | Cycle time: {self.duration} minutes.")
        monitor_thread = threading.Thread(target=self.monitor_directory)
        monitor_thread.daemon = True
        monitor_thread.start()