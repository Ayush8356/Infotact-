import os
import shutil

# Define the target directory
target_directory = 'path/target/directory'

# Define file type categories and their corresponding extensions
file_types = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv'],
}

# Create subdirectories for each file type
for folder in file_types.keys():
    folder_path = os.path.join(target_directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files into the corresponding folders
for filename in os.listdir(target_directory):
    file_path = os.path.join(target_directory, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
    
    # Determine the file type and move the file
    moved = False
    for folder, extensions in file_types.items():
        if any(filename.lower().endswith(ext) for ext in extensions):
            shutil.move(file_path, os.path.join(target_directory, folder, filename))
            moved = True
            break
    
    # If the file type is not recognized, move it to 'Others'
    if not moved:
        shutil.move(file_path, os.path.join(target_directory, 'Others', filename))

print("Files have been organized successfully.")
