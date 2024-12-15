import sys
import os
from secure_delete import secure_delete_file, secure_delete_directory

def main():
    """
    Main entry point for the secure delete tool.
    """
    if len(sys.argv) < 2:
        print("Usage: fr <path1> [path2 ... pathN]")
        sys.exit(1)

    targets = sys.argv[1:]  # Get all paths passed as arguments
    passes = 3  # Default number of overwrite passes

    for target_path in targets:
        if not os.path.exists(target_path):
            print(f"Error: {target_path} does not exist.")
            continue

        if os.path.isfile(target_path):
            secure_delete_file(target_path, passes)
        elif os.path.isdir(target_path):
            secure_delete_directory(target_path, passes)
        else:
            print(f"Error: {target_path} is not a valid file or directory.")

    print("Secure deletion completed for all specified targets.")

if __name__ == "__main__":
    main()
