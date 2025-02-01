import os
import logging

def secure_random_bytes(size):
    """
    Generates secure random bytes using os.urandom().
    """
    try:
        return os.urandom(size)
    except MemoryError:
        logging.error("Memory error occurred while generating secure random bytes.")
        return b''  # Return empty bytes on failure
    except OSError as err:
        logging.error(f"OS error while generating random bytes: {err}")
        return b''
