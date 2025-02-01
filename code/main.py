#!/usr/bin/env python3

import logging
from pathlib import Path
from argparse import ArgumentParser, Namespace
from secure_delete import secure_delete_file, secure_delete_directory, wipe_free_space

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main(args: Namespace):
    """
    Main entry point for the secure delete tool.
    """
    # If no files/directories are provided but --wipe is used, allow execution
    if not args.targets and not args.wipe:
        logging.error("No files or directories specified for deletion.")
        print("Usage: fr [-p PASSES] <file1> [file2 ...] [--wipe MOUNTPOINT]")
        exit(1)

    for target_path in args.targets:
        if not target_path.exists():
            logging.error(f"{target_path} does not exist.")
            continue

        if target_path.is_symlink():
            logging.warning(f"Skipping symbolic link: {target_path}")
            continue

        if target_path.is_file():
            secure_delete_file(target_path, args.p)
        elif target_path.is_dir():
            secure_delete_directory(target_path, args.p)
        else:
            logging.error(f"{target_path} is not a valid file or directory.")

    # Execute free space wipe if requested
    if args.wipe:
        wipe_free_space(args.wipe)

    logging.info("Secure deletion process completed.")

def _parse_args():
    parser = ArgumentParser(description="Secure file eraser for Linux. Deletes files and directories securely.")
    
    parser.add_argument('-p', type=int, default=3, required=False,
                        help="Number of passes to overwrite target data (default: 3)")
    
    parser.add_argument('targets', nargs='*', type=Path,  # Allow zero or more targets
                        help="Files or directories to securely delete")
    
    parser.add_argument('--wipe', type=str, required=False,
                        help="Wipe free space on the specified drive (e.g., /)")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = _parse_args()
    main(args)  # Now main() correctly handles --wipe without requiring targets
