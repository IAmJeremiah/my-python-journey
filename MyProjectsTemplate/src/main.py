import os

# Automatically gets your project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    print("Project initialized. BASE_DIR is:")
    print(BASE_DIR)

if __name__ == "__main__":
    main()
