"""
Class to contain all relevant information around the cameras
"""
class Camera():
    def __init__(self, name, address):
        self.camera_name = name
        self.camera_address = address
        self.camera_enabled = False

    def get_Address(self):
        return self.camera_address
    
    def get_Name(self):
        return self.camera_name
    
    def is_Enabled(self):
        return self.camera_enabled
    
    def set_Enable(self, state):
        self.camera_enabled = state

    def enable(self):
        self.camera_enabled = True
    
    def disable(self):
        self.camera_enabled = False

    def to_String(self):
        return "Camera: " + self.camera_name + "\nAddress: " + self.camera_address