"""
test_operate_menu.py
Test program for the interactive menu system using operate_menu from Utils.
"""

import os
import sys

# Add the root directory (C:\Data\Code) to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Utils import *  # Everything from __all__ in __init__.py is imported


def sine_power_series():
    print("\nSine function selected")


def cosine_power_series():
    print("\nCosine function selected")


def tangent_power_series():
    print("\nTangent function selected")


def main():
    menu_items = [
        ("[S] Sine", "S", "sine_power_series"),
        ("[C] Cosine", "C", "cosine_power_series"),
        ("[T] Tangent", "T", "tangent_power_series"),
        ("[Q] Quit", "Q", "QUIT")
    ]

    while True:
        selected_func = operate_menu(menu_items)
        if selected_func is None:
            break
        elif selected_func == "sine_power_series":
            sine_power_series()
        elif selected_func == "cosine_power_series":
            cosine_power_series()
        elif selected_func == "tangent_power_series":
            tangent_power_series()
        elif selected_func == "QUIT":
            print("\nExiting...")
            break
        #input("\nPress Enter to return to menu...")
        get_single_key("\nPress a key to return to menu...")



if __name__ == "__main__":
    main()
