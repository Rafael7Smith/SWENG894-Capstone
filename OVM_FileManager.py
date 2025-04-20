import os
import time

class OVM_FileManager():
    def __init__(self):
        pass


def get_directory_size(directory):
    """Calculate the total size of the directory in bytes."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_oldest_file(directory):
    """Get the oldest file in the directory."""
    oldest_file = None
    oldest_time = None
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            file_time = os.path.getctime(fp)
            if oldest_time is None or file_time < oldest_time:
                oldest_time = file_time
                oldest_file = fp
    return oldest_file

def manage_directory(directory, size_limit):
    """Monitor and manage the directory size."""
    while True:
        dir_size = get_directory_size(directory)
        print(f"Current directory size: {dir_size} bytes")
        
        if dir_size > size_limit:
            oldest_file = get_oldest_file(directory)
            if oldest_file:
                os.remove(oldest_file)
                print(f"Deleted oldest file: {oldest_file}")
            else:
                print("No files to delete.")
        else:
            print("Directory size is within the limit.")
        
        # Sleep for a minute before checking again
        time.sleep(60)