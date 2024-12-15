import os
import hashlib

def secure_random_bytes(size):
    """
    Generates secure random bytes using /dev/urandom and additional hashing.
    """
    random_data = os.urandom(size)
    hashed_data = hashlib.sha256(random_data).digest()
    return hashed_data[:size]
