import os

import shutil

# Define the path of the folder to organize
target_directory = os.path.expanduser(".") #~/Downloads
# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".bat", ".sh", ".apk"],
}

print (os.curdir)

#
def create_forders():
    for folder in file_types.keys():
        folders_path =os.path.join(target_directory,folder)
        if not os.path.exists(folders_path):
            os.mkdir(folders_path)
            #os.rmdir(folder_path) remove
            print(f"Create folder for ,[object Object],files")



def organize_files():
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        # Check if it's a file true or meta data,folder lai excape false
        if os.path.isfile(file_path):
            # file ko name rw .patxidi ko extendion lai split garxa
            _, extension = os.path.splitext(filename)
            moved = False

            # Match file to folder
            for folder, extensions in file_types.items():
                if extension.lower() in extensions:
                    shutil.move(file_path, os.path.join(target_directory, folder, filename))
                    # print(f"Moved ,{filename}, to ,{target_directory}\{folder},")
                    moved = True
                    break

            # If no match found, move to 'Others'
            if not moved:
                others_folder = os.path.join(target_directory, "Others")
                if not os.path.exists(others_folder):
                    os.mkdir(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved ,{filename}, to Others")

if __name__ == "__main__":
    create_forders()  # Create necessary folders
    organize_files()  # Organize files into folders
    print("Files organized successfully!")
