#8 Using os and time Modules:
import os
import time
def file_operations():
    os.makedirs("test_folder", exist_ok=True)
    print("Directory 'test_folder' created.")
    time.sleep(3)
    os.rmdir("test_folder")
    print("Directory 'test_folder' deleted.")
file_operations()