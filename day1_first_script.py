# Simple file organizer script

import os

# Folder you want to organize
folder = r"C:\Users\Jeremiah\Downloads"   # change this

# Create subfolders if they don't exist
file_types = {
    "images": [".jpg", ".png", ".jpeg"],
    "documents": [".pdf", ".docx", ".txt"],
    "archives": [".zip", ".rar"],
}

for item in os.listdir(folder):
    path = os.path.join(folder, item)

    # Skip folders
    if os.path.isdir(path):
        continue

    # Check extension
    _, ext = os.path.splitext(item)

    for category, extensions in file_types.items():
        if ext.lower() in extensions:
            target = os.path.join(folder, category)

            # Make folder if missing
            if not os.path.exists(target):
                os.makedirs(target)

            # Move file
            os.rename(path, os.path.join(target, item))
            print(f"Moved {item} → {category}")
