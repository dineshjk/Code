"""
menu_logic.py
Handles the interactive menu and triggers appropriate trigonometric functions based on user input.
"""

from keyboard_utils import clear_screen, wait_for_key
from keyboard_input import get_single_key
from math_utils import compute_and_display

menu_items = [
    ("[S] Sine", "SIN", "sine_power_series"),
    ("[C] Cosine", "COS", "cosine_power_series"),
    ("[T] Tangent", "TAN", "tangent_power_series"),
    ("[Q] Quit", "QUIT", None)
]

def menu():
    """ Displays the menu and handles
    user input to compute trigonometric functions."""
    index = 0
    while True:
        clear_screen()
        print("Choose a function to compute using power series:")
        for i, (label, _, _) in enumerate(menu_items):
            prefix = "-> " if i == index else "   "
            print(f"{prefix}{label}")

        key = get_single_key()
        key_lower = key.lower()

        if key == "\x1b":  # ESC key
            clear_screen()
            print("Exiting... Have a nice day!")
            break
        elif key == "\r":  # Enter key
            if menu_items[index][1] == "QUIT":
                clear_screen()
                print("Exiting... Have a nice day!")
                break
            index = compute_and_display(menu_items[index][1], menu_items[index][2])
        elif key == "\xe0":  # Special key prefix
            arrow_key = get_single_key()
            if arrow_key == "H":  # Up
                index = (index - 1) % len(menu_items)
            elif arrow_key == "P":  # Down
                index = (index + 1) % len(menu_items)
        elif key_lower in {'s', 'c', 't', 'q'}:
            index = {'s': 0, 'c': 1, 't': 2, 'q': 3}[key_lower]
            if key_lower == 'q':
                clear_screen()
                print("Exiting... Have a nice day!")
                break
            index = compute_and_display(menu_items[index][1], menu_items[index][2])
        else:
            print("\nWrong Key")
            wait_for_key("Press any key to continue...")
