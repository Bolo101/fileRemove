import os

def list_files(directory_path):
    """
    Lists all files in a directory and its subdirectories.
    """
    file_list = []
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_list.append(os.path.join(root, file_name))
    return file_list

def list_subdirectories(directory_path):
    """
    Lists all subdirectories in a directory.
    """
    subdirectories = []
    for root, dirs, _ in os.walk(directory_path):
        for dir_name in dirs:
            subdirectories.append(os.path.join(root, dir_name))
    return subdirectories
