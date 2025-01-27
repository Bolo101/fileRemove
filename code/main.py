#!/usr/bin/env python3

from pathlib import Path
from argparse import ArgumentParser
from secure_delete import secure_delete_file, secure_delete_directory

def main(passes : int, targets : Path):
    """
    Main entry point for the secure delete tool.
    """
    for target_path in targets:
        if not target_path.exists():
            print(f"Error: {target_path} does not exist.")
            continue

        if target_path.is_file():
            secure_delete_file(target_path, passes)
        elif target_path.is_dir():
            secure_delete_directory(target_path, passes)
        else:
            print(f"Error: {target_path} is not a valid file or directory.")

    print("Secure deletion completed for all specified targets.")

def _parse_args():
    parser = ArgumentParser(description="Secure file eraser to run in terminal. Delete both files and directories")
    parser.add_argument('-p',
                        help="Number of passes to overwrite target data",
                        type=int,
                        default=7,
                        required=False)
    parser.add_argument('targets', 
                        nargs='*',
                        help="Files or directories to securely delete")
    return parser.parse_args()

if __name__ == "__main__":
    args = _parse_args()

    if not args.targets:
        print("Error: No files or directories specified for deletion.")
        print("Usage: fr [-p PASSES] <file1> [file2 ...] [-p PASSES]")
        exit(1)

    main(args.p, args.targets)
