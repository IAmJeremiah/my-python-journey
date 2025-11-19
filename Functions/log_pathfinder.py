import os
# Get the folder where THIS script lives
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build a full path to system.log in the same folder
log_path = os.path.join(base_dir, "system.log")
print("Log file path:", log_path)