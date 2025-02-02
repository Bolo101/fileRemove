# Secure File Deletion Tool

A Python-based command-line utility for secure deletion of files and directories. This tool ensures that deleted data cannot be recovered by overwriting it with multiple passes of random data followed by zero-padding.

## Features

- **Secure Random Data Overwriting**: Uses a strong secure random number generator to overwrite files and directories with random data.
- **Zero Data Pass**: Ensures data is irrecoverable by applying a final pass of zeros.
- **Batch File & Directory Deletion**: Securely deletes multiple files and directories in a single command.
- **Subdirectory Handling**: Recursively deletes all contents within directories, including subdirectories.
- **Hard Link Detection**: Warns if a file has multiple hard links, as the data may still be recoverable elsewhere.
- **Symbolic Link Protection**: Prevents accidental deletion of symbolic links.
- **Free Space Wiping**: Option to wipe all free space on a specified drive to prevent data recovery.

## Prerequisites

- Python **3.6 or later**
- Linux operating system

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Bolo101/fileRemove.git
   cd fileRemove/code
   ``

2. Ensure the script is executable:

   ```bash
   chmod +x main.py
   ```

3. Create a symbolic link to use the tool as a system-wide command (`fr`):

   ```bash
   sudo ln -s $(pwd)/main.py /usr/local/bin/fr
   ```

   You can now use the tool with the `fr` command.

## Usage

### Securely Delete Files

To securely delete files:

```bash
fr file1.txt file2.txt
```

### Securely Delete Directories

To securely delete a directory and its contents:

```bash
fr folder_name
```

### Securely Delete Multiple Files and Directories

You can mix files and directories in the same command:

```bash
fr file1.txt folder_name file2.log
```

### Specify Overwrite Passes

By default, the tool performs 3 passes of overwriting. To specify a custom number of passes:

```bash
fr -p 7 secret.txt
```
This will overwrite *secret.txt* 5 times before deleting it.

### Wipe Free Space

To securely wipe all free space on a drive (e.g., / for the root filesystem):

```bash
fr --wipe /
```

⚠️ Warning: This process will fill up the disk temporarily. Ensure you have enough space.


### Command Help

Use the `--help` flag to display usage information:

```bash
fr --help
```

## Code Structure

```bash
project/
├── README.md                    # Documentation for the project
├── code/                
    ├── main.py                  # Entry point for the CLI tool
    ├── secure_delete.py         # Logic for secure deletion of files and directories
    ├── file_operations.py       # Functions for file and directory operations
    ├── random_generator.py      # Secure random number generator implementation
├── LICENSE                      # LICENSE
```

## License

This project is licensed under the Creative Commons 4 License - see the LICENSE file for details.