"""
keyboard_utils.py
Utility functions for clearing the screen and pausing execution for keypress.
"""

import os
import msvcrt

def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def wait_for_key(message="Press any key to continue..."):
    """Displays a message and waits for any keypress."""
    print(message)
    while True:
        key = msvcrt.getch()
        key_lower = key.lower()
        if key:
            break
