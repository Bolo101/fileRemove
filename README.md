
# Secure File Deletion Tool

A Python-based command-line utility for secure deletion of files and directories. This tool ensures that deleted data cannot be recovered by overwriting it with multiple passes of random data followed by zero-padding.

## Features

- **Secure Random Data Overwriting**: Utilizes a custom secure random number generator to overwrite files and directories with random data.
- **Zero Data Pass**: Completes the deletion process by overwriting data with zeros.
- **Batch File Deletion**: Allows secure deletion of multiple files or directories in a single command.
- **Subdirectory Handling**: Automatically detects and securely deletes all contents within directories, including subdirectories.

## Prerequisites

- Python 3.6 or later
- Linux operating system

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/secure-delete.git
   cd secure-delete
   ```

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
```


## License

This project is licensed under the Creative Common 4 License - see the LICENSE file for details.
