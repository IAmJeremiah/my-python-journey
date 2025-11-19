import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Create a text file and write to it
file_path = os.path.join(BASE_DIR, "notes.txt")

with open(file_path, "w") as file:
    file.write("This is your first line.\n")
    file.write("This is your second line.\n")

print("File created and written to:", file_path)

# 2. Read the file back
with open(file_path, "r") as file:
    contents = file.read()

print("\n=== File Contents ===")
print(contents)
