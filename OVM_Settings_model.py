import os

class OVM_Settings():
    def __init__(self):
        #Default save path is current directory
        self.savePath = ""

    def getSavePath(self):
        return self.savePath