import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "D:/Python/Project103/folder"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} Has been created!")

    def on_deleted(self, event):
        print(f"Oops someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"{event.src_path} has been modified!")

    def on_moved(self, event):
        print(f"You have moved or renamed {event.src_path}!")
    

eventHandler = FileEventHandler()
observer = Observer()

observer.schedule(eventHandler,from_dir,recursive=False)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running ...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()