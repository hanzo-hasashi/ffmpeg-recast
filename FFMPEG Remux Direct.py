# Use this script to convert AVI files to MP4 (copies video container & converts audio to AAC codec)
# Tested & works on AVI files

import os
import subprocess

# VARIABLES
SOURCE_FOLDER  = r'C:\Users\arahi\Desktop\Unsorted' # Directory containing Video files
DESTINATION_FOLDER = os.path.join(SOURCE_FOLDER, "Remux Files") # Set the destination directory
FILE_EXTENSIONS = ('.avi', '.mkv', '.m4v', '.mp4') # Define file types

# Create 'DESTINATION_FOLDER' folder if it doesn't exist
if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

# Loop through all files in the directory
for filename in os.listdir(SOURCE_FOLDER):
    if filename.lower().endswith(FILE_EXTENSIONS):
        input_file = os.path.join(SOURCE_FOLDER, filename)
        # output_file = os.path.join(SOURCE_FOLDER, 'Remuxed', f"{os.path.splitext(filename)[0]}.mp4")
        output_file = os.path.join(DESTINATION_FOLDER, f"{os.path.splitext(filename)[0]}.mp4")

        # ffmpeg command to convert avi to mp4
        # command = f'ffmpeg.exe -i "{input_file}" -c:v copy -c:a aac "{output_file}"' # Audio conversion to AAC
        command = f'ffmpeg.exe -i "{input_file}" -c:v copy -c:a copy -map_metadata 0 "{output_file}"' # Remux

        # Run the ffmpeg command using subprocess
        subprocess.run(command, shell=True)