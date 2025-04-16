# Utils/menu_utils.py

"""
menu_utils.py

Provides utilities to show and operate a UI-style keyboard-driven menu using arrow keys,
hotkeys, Enter, Escape. Returns the function name or identifier of the selected item.
"""
import os
import sys
import io
from Utils.keyboard_utils import clear_screen, get_single_key

__all__ = ['show_menu', 'operate_menu']

def show_menu(menu_items, selected_index, begin_message="Menu", end_message = "Select Option"):
    """
    Displays the menu with the selected item highlighted.
    """
    clear_screen()
    print(begin_message, end='\n', flush=True)
    for index, (label, hotkey, _) in enumerate(menu_items):
        if index == selected_index:
            print(f">> {label} <<")
        else:
            print(f"   {label}")


def operate_menu(menu_items, begin_message="Menu", end_message = "Select Option"):
    """
    Operates a keyboard-driven menu.
    Returns the function name associated with the selected menu item.
    Returns None if the user cancels via Escape or selects Quit.
    """

    selected_index = 0

    # Extract valid keys from menu items
    valid_keys = ['UP', 'DOWN', 'ENTER', 'ESC'] + [hotkey.upper() for _, hotkey, _ in menu_items]
    valid_keys += [hotkey.lower() for _, hotkey, _ in menu_items]

    while True:
        show_menu(menu_items, selected_index, begin_message, end_message)
        key = get_single_key("Your choice: ", valid_keys)

        if key == 'UP':
            selected_index = (selected_index - 1) % len(menu_items)
        elif key == 'DOWN':
            selected_index = (selected_index + 1) % len(menu_items)
        elif key == 'ESC':
            clear_screen()
            #print(original_screen, end="")
            return None
        elif key == 'ENTER':
            label, hotkey, func_name = menu_items[selected_index]
            clear_screen()
            #print(original_screen, end="")
            return func_name
        else:
            for i, (_, hotkey, func_name) in enumerate(menu_items):
                if key.upper() == hotkey.upper():
                    clear_screen()
                    #print(original_screen, end="")
                    return func_name
