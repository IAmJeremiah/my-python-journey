#Step 1: Use BASE_DIR to build the path to notes.txt
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "notes.txt")

#✔ Step 2: Append these lines to the file:
open(file_path, "a")
with open(file_path, "a")as files:
    files.write("Third line added. \n")
    files.write("Fourth line added. \n")
#This will add:
#Third line added.
#Fourth line added.


#Step 3: Read the file line by line (using for line in file:)
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())
    file.close()


#✔ Step 4: Print each line with a line number:
with open(file_path, "r") as file:
    for idx, line in enumerate(file, start=1):
        print(f"#{idx}: {line.strip()}")
#This will output:
#1: This is your first line.
#2: This is your second line.
#3: Third line added.
#4: Fourth line added.

#Example output:
#1: This is your first line.
#2: This is your second line.
#3: Third line added.
#4: Fourth line added.
