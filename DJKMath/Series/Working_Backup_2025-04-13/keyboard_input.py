"""
keyboard_input.py
Handles capturing single key input from user.
"""

import msvcrt

def get_single_key():
    """Returns a single character from the keyboard (handles special keys too)."""
    key = msvcrt.getch()
    if key == b'\xe0' or key == b'\x00':
        return '\xe0'  # Special key prefix
    return key.decode()
