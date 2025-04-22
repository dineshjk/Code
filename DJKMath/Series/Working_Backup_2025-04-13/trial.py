""" Trial code to test the keyboard_utils module """
from  Utils import keyboard_utils as kb #

a = kb.get_single_key("Press any key to continue...")
print("You pressed:", a)