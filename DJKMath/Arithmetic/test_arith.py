"""
test_arith.py
This is a test file for the arithmetic module in the DJKMath package.
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

from Utils import get_integer,clear_screen, get_single_key


import time
from number_theory import factorial, factorial_recursive

def test_performance(n):
    # Test iterative
    start = time.time()
    factorial(n)
    iter_time = time.time() - start

    # Test recursive
    start = time.time()
    factorial_recursive(n)
    rec_time = time.time() - start

    print(f"n = {n}")
    print(f"Iterative: {iter_time:.6f} seconds")
    print(f"Recursive: {rec_time:.6f} seconds")


if __name__ == '__main__':
    """ Here we write a program for factorial of a number.
    The number is taken from the user and the factorial is calculated using recursion.
    The program is tested using the test_arith.py file.
    """

    clear_screen()
    # Code for testing here.
    # Test with different sizes
    for n in [5, 10, 100, 500]:
        test_performance(n)
        get_single_key()
