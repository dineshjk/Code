"""
keyboard_utils.py
This module provides utility functions for keyboard interaction,
including keypress detection and screen clearing.


To call it from a module, say C:/Data/Code/Math/Arithmetic\all_divisors.py
do the following. In that module, add the following lines:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Utils')))
from Utils.keyboard_utils import clear_screen
"""

__all__ = ['clear_screen', 'get_single_key', 'wait_for_key']

import os
import msvcrt
import sys

def clear_screen():
    """Clears the terminal screen (Windows or Unix)."""
    os.system("cls" if os.name == "nt" else "clear")

def wait_for_key(message="Press a key to continue..."):
    """[DEPRECATED] Displays a message and waits for a keypress.
    Use get_single_key instead.
    """
    print("wait_for_key is deprecated. Use get_single_key instead.", end='', flush=True)
    print(message, end='', flush=True)
    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            break
    while msvcrt.kbhit():
        msvcrt.getch()
    sys.stdout.write('\r' + ' ' * len(message) + '\r')
    sys.stdout.flush()



def get_single_key(message="", valid_keys=None):
    """Wait for a single valid keypress and return its name.
    If valid_keys is provided, repeat until one of them is pressed.
    Message is displayed before prompting.
    The prompt is cleared after key is pressed.
    """
    special_keys = {
        b'H': 'UP', b'P': 'DOWN', b'K': 'LEFT', b'M': 'RIGHT',
        b';': 'F1', b'<': 'F2', b'=': 'F3', b'>': 'F4',
        b'?': 'F5', b'@': 'F6', b'A': 'F7', b'B': 'F8',
        b'C': 'F9', b'D': 'F10', b'\x85': 'F11', b'\x86': 'F12'
    }

    def decode_key(key, is_extended):
        if is_extended:
            return special_keys.get(key, f'SPECIAL_{key.hex()}')
        if key == b'\r':
            return 'ENTER'
        if key == b'\x1b':
            return 'ESC'
        try:
            return key.decode().upper() if key.isalpha() else key.decode()
        except UnicodeDecodeError:
            return f'UNKNOWN_{key.hex()}'

    if message:
        print(message, end='', flush=True)

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            is_extended = key in (b'\x00', b'\xe0')
            key = msvcrt.getch() if is_extended else key
            key_name = decode_key(key, is_extended)

            while msvcrt.kbhit():
                msvcrt.getch()

            if (valid_keys is None) or (key_name in valid_keys):
                print()
                return key_name
