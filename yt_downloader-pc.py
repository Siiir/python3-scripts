# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 01:50:31 2022

@author: HP
"""

import os
import subprocess
import threading

import pytube

LINK= None
NEW_FILENAME= None

link= LINK or input("Enter video link:")
movie = pytube.YouTube(link)

streams= movie.streams
filt_streams= streams.filter(mime_type="audio/mp4")

stream_idx = -1; print(filt_streams[stream_idx])
parent_dir = os.path.join(
    os.getenv("userprofile"), r"Downloads",
)
# Start downloading
downloading_thread= threading.Timer(0, lambda: filt_streams[stream_idx].download(parent_dir), print("Downloaded!"))
downloading_thread.start()
# But prompt user for file name at the same time
new_filename = NEW_FILENAME or input("Enter filename (including extension): ")  # e.g. new_filename.mp3
downloading_thread.join()

#%%%

default_filename = filt_streams[stream_idx].default_filename  # get default name using pytube API
subprocess.run([
    'ffmpeg',
    '-i', os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('Done !')