import os
from utils.helpers import hello

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    print("Project initialized.")
    print("BASE_DIR:", BASE_DIR)
    print(hello("Jeremiah"))

if __name__ == "__main__":
    main()
