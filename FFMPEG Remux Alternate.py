# Use this script to move video files to "YYYY\MMYY" folder (example 2019\0119 January) this date is extracted from QuickTime tag
# Tested, works on Image (EXIF tag) & Video (QuickTime tag) files

import os
import subprocess

# VARIABLES
SOURCE_FOLDER  = r'C:\Users\arahi\Desktop\Unsorted' # Directory containing Video files
DESTINATION_FOLDER = os.path.join(SOURCE_FOLDER, "Remux Alt Files") # Set the destination directory
FILE_EXTENSIONS = ('.avi', '.mkv', '.m4v', '.mp4') # Define file types

# Create 'DESTINATION_FOLDER' folder if it doesn't exist
if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

def convert_video_to_mp4(input_path, output_path):
    # Construct the ffmpeg command
    command = [
        'ffmpeg',
        '-i', input_path,
        '-c:v', 'copy',
        '-c:a', 'copy',
        '-map_metadata', '0',
        output_path
    ]

    # Run the ffmpeg command
    subprocess.run(command)

def convert_all_files(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter for Video files
    video_files = [file for file in files if file.lower().endswith(FILE_EXTENSIONS)]

    # Process each Video file
    for video_file in video_files:
        input_path = os.path.join(folder_path, video_file)
        output_path = os.path.join(DESTINATION_FOLDER, os.path.splitext(video_file)[0] + '.MP4')
        convert_video_to_mp4(input_path, output_path)

if __name__ == "__main__":
    # Run the conversion for all Video files in the folder
    convert_all_files(SOURCE_FOLDER)