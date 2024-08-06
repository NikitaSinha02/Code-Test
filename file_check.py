# -*- coding: utf-8 -*-


import os
import glob
import shutil

def check_files(folder_path, processed_files, invalid_folder):
    # Get all files in the folder with .csv extension
    all_files = glob.glob(os.path.join(folder_path, "*.csv"))
    valid_files = []

    for file in all_files:
        file_name = os.path.basename(file)

        # Check if the file is new
        if file_name in processed_files:
            print(f"Skipping already processed file: {file_name}")
            continue

        # Check if the file is empty
        if os.path.getsize(file) == 0:
            print(f"File is empty: {file_name}")
            shutil.move(file, os.path.join(invalid_folder, file_name))
            continue
        
        valid_files.append(file)

    return valid_files

# Example usage:
if __name__ == "__main__":
    folder_path = "D:/Zomato"
    invalid_folder = "C:/Users/akash/Zomato Daily/invalid_files"
    processed_files = set()

    if not os.path.exists(invalid_folder):
        os.makedirs(invalid_folder)

    valid_files = check_files(folder_path, processed_files, invalid_folder)
    print(f"Valid files: {valid_files}")