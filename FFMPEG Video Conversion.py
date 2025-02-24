# Use this script to Convert Video files to H264 MP4 with relatively good quality (bitrate 10 mbps)

import os
import subprocess

# VARIABLES
SOURCE_FOLDER  = r'C:\Users\arahi\Desktop\Unsorted' # Directory containing Video files
DESTINATION_FOLDER = os.path.join(SOURCE_FOLDER, "Converted Files") # Set the destination directory
FILE_EXTENSIONS = ('.mp4') # Define file types

# Loop through all files in the directory
for filename in os.listdir(SOURCE_FOLDER):
    if filename.lower().endswith('.mp4'):
        input_file = os.path.join(SOURCE_FOLDER, filename)
        if not os.path.exists(DESTINATION_FOLDER):
            os.makedirs(DESTINATION_FOLDER)
        output_file = os.path.join(DESTINATION_FOLDER, f"{filename}")
        
        # ffmpeg command to convert avi to mp4
        command = f'ffmpeg.exe -i "{input_file}" -c:v h264_nvenc -b:v 10M -c:a copy -map_metadata 0 "{output_file}"' # Adjust 10M for bitrate
        
        # Run the ffmpeg command using subprocess
        subprocess.run(command, shell=True)