"""
Test suite for input/output utilities.
Tests all functions from Utils.inout module with various scenarios.
"""

import sys
import os



# from Utils.keyboard_utils import get_single_key

# Add parent directory to Python path to find Utils package
#sys.path.append(".")
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# According to many help files the least preferred and volatile is first one.
# The second is robust
# The third is the most robust and preferred.

from Utils import get_bunch_complex,clear_screen, get_single_key



if __name__ == '__main__':

    clear_screen()
    # Code for testing here.
    mylist = []
    get_bunch_complex(mylist,3)
    print(f"The numbers you entered are: {mylist}")
    print("Press any key to continue...")
    get_single_key()