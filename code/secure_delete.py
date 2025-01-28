from random_generator import secure_random_bytes
from pathlib import Path

def secure_delete_file(file_path: Path, passes: int):
    """
    Securely deletes a file by overwriting its content multiple times.
    """
    try:
        if not file_path.is_file():
            print(f"{file_path} is not a valid file.")
            return

        file_size = file_path.stat().st_size
        for pass_num in range(passes):
            print(f"Overwriting {file_path} with random data (pass {pass_num + 1}/{passes})...")
            file_path.write_bytes(secure_random_bytes(file_size))
        print(f"Overwriting {file_path} with zeros...")
        file_path.write_bytes(b'\x00' * file_size)

        file_path.unlink()
        print(f"File {file_path} securely deleted.")
    except Exception as e:
        print(f"Error securely deleting file {file_path}: {e}")

def secure_delete_directory(directory_path : Path, passes: int):
    """
    Securely deletes all files and subdirectories within a directory.
    """
    try:
        if not directory_path.is_dir():
            print(f"{directory_path} is not a valid directory.")
            return

        for root, dirs, files in directory_path.walk(top_down=False):
            for file_name in files:
                secure_delete_file((root / file_name), passes)
            for dir_name in dirs:
                (root / dir_name).rmdir()

        directory_path.rmdir()
        print(f"Directory {directory_path} securely deleted.")
    except Exception as e:
        print(f"Error securely deleting directory {directory_path}: {e}")
