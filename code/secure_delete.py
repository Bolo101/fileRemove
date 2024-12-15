import os
from random_generator import secure_random_bytes

def secure_delete_file(file_path, passes=3):
    """
    Securely deletes a file by overwriting its content multiple times.
    """
    try:
        if not os.path.isfile(file_path):
            print(f"{file_path} is not a valid file.")
            return

        file_size = os.path.getsize(file_path)
        with open(file_path, "wb") as f:
            for pass_num in range(passes):
                print(f"Overwriting {file_path} with random data (pass {pass_num + 1}/{passes})...")
                f.write(secure_random_bytes(file_size))
                f.flush()
            print(f"Overwriting {file_path} with zeros...")
            f.write(b'\x00' * file_size)
            f.flush()

        os.remove(file_path)
        print(f"File {file_path} securely deleted.")
    except Exception as e:
        print(f"Error securely deleting file {file_path}: {e}")

def secure_delete_directory(directory_path, passes=3):
    """
    Securely deletes all files and subdirectories within a directory.
    """
    try:
        if not os.path.isdir(directory_path):
            print(f"{directory_path} is not a valid directory.")
            return

        for root, dirs, files in os.walk(directory_path, topdown=False):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                secure_delete_file(file_path, passes)
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                os.rmdir(dir_path)

        os.rmdir(directory_path)
        print(f"Directory {directory_path} securely deleted.")
    except Exception as e:
        print(f"Error securely deleting directory {directory_path}: {e}")
