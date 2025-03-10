class Camera():
    def __init__(self, name, address):
        self.camera_name = name
        self.camera_address = address

    def get_Address(self):
        return self.camera_address
    
    def get_Name(self):
        return self.camera_name
    
    def enable(self):
        self.camera_enabled = True
    
    def disable(self):
        self.camera_enabled = False

    def to_String(self):
        return "Camera: " + self.camera_name + "\nAddress: " + self.camera_address