import os
import logging
from random_generator import secure_random_bytes
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def secure_delete_file(file_path: Path, passes: int):
    """
    Securely deletes a file by overwriting its content multiple times.
    """
    if not file_path.is_file():
        logging.error(f"{file_path} is not a valid file.")
        return

    # Detect and warn about hard links
    try:
        if file_path.stat().st_nlink > 1:
            logging.warning(f"{file_path} has multiple hard links. Data may still be recoverable.")
    except FileNotFoundError:
        logging.error(f"File not found during hard link check: {file_path}")
        return
    except PermissionError:
        logging.error(f"Permission denied when checking hard links for {file_path}")
        return

    file_size = file_path.stat().st_size

    for pass_num in range(passes):
        try:
            logging.info(f"Overwriting {file_path} with random data (pass {pass_num + 1}/{passes})...")
            with open(file_path, 'wb') as f:
                f.write(secure_random_bytes(file_size))
        except FileNotFoundError:
            logging.error(f"File not found while overwriting: {file_path}")
            return
        except PermissionError:
            logging.error(f"Permission denied while overwriting: {file_path}")
            return
        except OSError as err:
            logging.error(f"OS error while overwriting {file_path}: {err}")
            return

    try:
        logging.info(f"Overwriting {file_path} with zeros for final pass...")
        with open(file_path, 'wb') as f:
            f.write(b'\x00' * file_size)
    except FileNotFoundError:
        logging.error(f"File not found during zero overwrite: {file_path}")
        return
    except PermissionError:
        logging.error(f"Permission denied during zero overwrite: {file_path}")
        return

    try:
        file_path.unlink()
        logging.info(f"File {file_path} securely deleted.")
    except FileNotFoundError:
        logging.error(f"File already deleted: {file_path}")
    except PermissionError:
        logging.error(f"Permission denied while deleting file: {file_path}")

    # Verify deletion
    if file_path.exists():
        logging.warning(f"Warning: {file_path} was not successfully deleted.")

def secure_delete_directory(directory_path: Path, passes: int):
    """
    Securely deletes all files and subdirectories within a directory.
    """
    if not directory_path.is_dir():
        logging.error(f"{directory_path} is not a valid directory.")
        return

    for root, dirs, files in os.walk(directory_path, topdown=False):
        root_path = Path(root)

        for file_name in files:
            secure_delete_file(root_path / file_name, passes)

        for dir_name in dirs:
            try:
                (root_path / dir_name).rmdir()
            except FileNotFoundError:
                logging.error(f"Directory not found: {root_path / dir_name}")
            except PermissionError:
                logging.error(f"Permission denied while deleting directory: {root_path / dir_name}")

    try:
        directory_path.rmdir()
        logging.info(f"Directory {directory_path} securely deleted.")
    except FileNotFoundError:
        logging.error(f"Directory already deleted: {directory_path}")
    except PermissionError:
        logging.error(f"Permission denied while deleting directory: {directory_path}")

    # Verify deletion
    if directory_path.exists():
        logging.warning(f"Warning: {directory_path} was not successfully deleted.")

def wipe_free_space(mount_point: str):
    """
    Wipes free space on a given filesystem by writing large temporary files.
    """
    temp_file = Path(mount_point) / "wipe_temp"
    
    logging.info(f"Starting free space wipe on {mount_point}...")
    try:
        with open(temp_file, 'wb') as f:
            try:
                while True:
                    f.write(secure_random_bytes(1024 * 1024))  # Write 1MB at a time
            except OSError:
                pass  # Stop when disk is full
    except FileNotFoundError:
        logging.error(f"Mount point {mount_point} not found.")
        return
    except PermissionError:
        logging.error(f"Permission denied while wiping free space on {mount_point}")
        return
    except OSError as err:
        logging.error(f"OS error during free space wipe on {mount_point}: {err}")
        return

    try:
        temp_file.unlink()
        logging.info("Free space wipe completed.")
    except FileNotFoundError:
        logging.error(f"Temporary wipe file not found: {temp_file}")
    except PermissionError:
        logging.error(f"Permission denied while deleting temporary wipe file: {temp_file}")
