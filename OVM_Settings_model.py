import os
from configparser import ConfigParser

"""
Settings management class, responsible for saving and loading settings from a "settings.ini" file
"""
class OVM_Settings():
    def __init__(self, config_file='settings.ini'):
        self.config_file = config_file
        self.config = ConfigParser()

        # Default values
        self.video_feeds = 4
        self.enable_saving = False
        self.save_location = ''
        self.save_size = 0
        self.file_size = 0
        self.camera_model = {}

        #Check if settings file exists, if not create it
        if os.path.exists(self.config_file):
            self.load_settings()

    def load_settings(self):
        """Load settings from the config file."""
        self.config.read(self.config_file)

        if 'Settings' in self.config:
            self.video_feeds = self.config.getint('Settings', 'VideoFeeds', fallback=self.video_feeds)
            self.enable_saving = self.config.getboolean('Settings', 'EnableSaving', fallback=self.enable_saving)
            self.save_location = self.config.get('Settings', 'SaveLocation', fallback=self.save_location)
            self.save_size = self.config.getint('Settings', 'SaveSize', fallback=self.save_size)
            self.file_size = self.config.getint('Settings', 'FileSize', fallback=self.file_size)

        if 'CameraModel' in self.config:
            for key in self.config['CameraModel']:
                ip, status = self.config.get('CameraModel', key).split(',')
                self.camera_model[key] = (ip, status)

    def save_settings(self):
        """Save the current settings to the config file."""
        if 'Settings' not in self.config:
            self.config.add_section('Settings')

        self.config.set('Settings', 'VideoFeeds', str(self.video_feeds))
        self.config.set('Settings', 'EnableSaving', str(self.enable_saving))
        self.config.set('Settings', 'SaveLocation', self.save_location)
        self.config.set('Settings', 'SaveSize', str(self.save_size))
        self.config.set('Settings', 'FileSize', str(self.file_size))

        if 'CameraModel' not in self.config:
            self.config.add_section('CameraModel')

        for camera_name, (ip, status) in self.camera_model.items():
            self.config.set('CameraModel', camera_name, f'{ip},{status}')

        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def get_VideoFeed(self):
        return self.video_feeds
    
    def get_EnableSaving(self):
        return self.enable_saving
    
    def get_Savelocation(self):
        return self.save_location

    def get_SaveSize(self):
        return self.save_size

    def get_FileSize(self):
        return self.file_size

    def get_CameraModel(self):
        return self.camera_model
    
    def set_VideoFeed(self, feeds):
        self.video_feeds = feeds

    def set_EnableSaving(self, saving):
        self.enable_saving = saving

    def set_SaveLocation(self, location):
        self.save_location = location

    def set_SaveSize(self, size):
        self.save_size = size

    def set_FileSize(self, size):
        self.file_size = size

    def set_CameraModel(self, camera_name, ip_address, status):
        self.camera_model[camera_name] = (ip_address, status)
    
    def to_String(self):
        return f"Settings Model. Video Feeds: {self.video_feeds} | Save Location: {self.save_location} | Save Size: {self.save_size} | Recording Size: {self.file_size} | Cameras: {self.camera_model}"