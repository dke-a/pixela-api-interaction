import hashlib
import os

def get_hashed_token(token):
    """Returns the provided token."""
    # Initially created to do perform hashing, but now just returns the token.
    return token

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
