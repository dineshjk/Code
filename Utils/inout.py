"""
inout.py
This is a input output module in my package. C:/Data/Code/Utils/inout.py

To call it from a module, say C:/Data/Code/Math/Arithmetic\all_divisors.py
do the following. In that module, add the following lines:
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from math import sqrt
from Utils import get_integer

"""

from requests import get
from .keyboard_utils import clear_screen, get_single_key, wait_for_key

def get_integer(constraint=None, message="Enter an integer: ", range_min=None, range_max=None):
    """
    Prompt the user for an integer with optional constraints.

    Parameters:
    -----------
    constraint : str, optional
        Type of constraint to apply:
        - "positive": Only accept positive integers (> 0)
        - "negative": Only accept negative integers (< 0)
        - None: Accept any integer
    message : str, optional
        Custom prompt message to display to the user
    range_min : int, optional
        Minimum value (inclusive) for the integer input
    range_max : int, optional
        Maximum value (inclusive) for the integer input

    Returns:
    --------
    int
        The validated integer input that meets the specified constraint

    Raises:
    -------
    ValueError
        If the input cannot be converted to an integer
        If the range constraints are invalid (min > max)
    KeyboardInterrupt
        If the user cancels the input (Ctrl+C)
    RuntimeError
        If an unexpected error occurs during input processing

    Examples:
    --------
    >>> num = get_integer(range_min=1, range_max=10)  # Gets number between 1 and 10
    >>> num = get_integer("positive")                 # Gets any positive number
    >>> num = get_integer(range_min=0, range_max=100) # Gets number between 0 and 100
    """
    # Validate range constraints
    if range_min is not None and range_max is not None:
        if range_min > range_max:
            raise ValueError(f"Invalid range: min ({range_min}) cannot be greater than max ({range_max})")
        message = f"{message} [{range_min}-{range_max}]: "

    while True:
        try:
            value = int(input(message).strip())

            # Check range constraints
            if range_min is not None and value < range_min:
                print(f"Please enter a number greater than or equal to {range_min}.")
                continue
            if range_max is not None and value > range_max:
                print(f"Please enter a number less than or equal to {range_max}.")
                continue

            # Check other constraints
            if constraint == "positive" and value <= 0:
                print("Please enter a positive integer (greater than 0).")
                continue
            if constraint == "negative" and value >= 0:
                print("Please enter a negative integer (less than 0).")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter an integer only.")
            raise ValueError("Input must be an integer")
        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
            raise KeyboardInterrupt("Input operation cancelled by user")
        except Exception as e:
            error_msg = f"Unexpected error during integer input: {str(e)}"
            print(error_msg)
            raise RuntimeError(error_msg) from e

def get_float(constraint=None, message="Enter a real number: ", range_min=None, range_max=None):
    """
    Prompt the user for a float with optional constraints.

    Parameters:
    -----------
    constraint : str, optional
        Type of constraint to apply:
        - "positive": Only accept positive numbers (> 0)
        - "negative": Only accept negative numbers (< 0)
        - None: Accept any number
    message : str, optional
        Custom prompt message to display to the user
    range_min : float, optional
        Minimum value (inclusive) for the float input
    range_max : float, optional
        Maximum value (inclusive) for the float input

    Returns:
    --------
    float
        The validated float input that meets the specified constraint

    Raises:
    -------
    ValueError
        If the input cannot be converted to a float
        If the range constraints are invalid (min > max)
    """
    # Validate range constraints
    if range_min is not None and range_max is not None:
        if range_min > range_max:
            raise ValueError(f"Invalid range: min ({range_min}) cannot be greater than max ({range_max})")
        message = f"{message} [{range_min}-{range_max}]: "

    try:
        value = float(input(message).strip())

        # Check range constraints
        if range_min is not None and value < range_min:
            raise ValueError(f"Value must be greater than or equal to {range_min}")
        if range_max is not None and value > range_max:
            raise ValueError(f"Value must be less than or equal to {range_max}")

        # Check other constraints
        if constraint == "positive" and value <= 0:
            raise ValueError("Value must be positive")
        if constraint == "negative" and value >= 0:
            raise ValueError("Value must be negative")

        return value

    except ValueError as e:
        print("Invalid input. Please enter a number only.")
        raise ValueError(str(e))

def get_complex(message="Enter a complex number (a + bj): "):
    """
    Prompt the user for a complex number in the form a + bj.

    Parameters:
    -----------
    message : str, optional
        Custom prompt message to display to the user

    Returns:
    --------
    complex
        The validated complex number input

    Raises:
    -------
    ValueError
        If the input cannot be converted to a complex number
    """
    try:
        value = input(message).strip().replace(" ", "")
        # Handle input without imaginary part
        if 'j' not in value:
            return complex(float(value), 0)
        return complex(value)
    except ValueError:
        print("Invalid input. Please enter a complex number in the form a+bj")
        print("Examples: 3+4j, 1-2j, 5 (for real numbers)")
        raise ValueError("Invalid complex number format")

def get_bunch_integers(numbers, n=None):
    """
    Reads integers from the user and appends them to the given list 'numbers'.

    Parameters:
    - numbers (list): A list to which read integers will be appended.
    - n (int, optional): If provided, the function reads exactly 'n' integers.
                         If not provided or None, it reads integers until a non-integer is entered.

    Behavior:
    - Prompts the user to enter each integer individually.
    - For fixed input count (n is given): continues until 'n' integers are entered or
      user enters a non-integer.
    - For open-ended input (n is None): continues until a non-integer is entered.
    - Displays a user-friendly prompt and clears the screen between inputs.

    Returns:
    - list: The updated list 'numbers' containing the integers entered by the user.
    """
    count = 0
    while True:
        clear_screen()
        if n is not None:
            print(f"Enter integer number {count + 1} of {n} (or anything else to cancel):")
        else:
            print(f"Enter integer number {count + 1} (or anything else to stop):")

        entry = input(">> ")
        try:
            number = int(entry)
            numbers.append(number)
            count += 1
            if n is not None and count >= n:
                print("\nMaximum number of integers reached.")
                get_single_key("Press any key to continue...")
                break
        except ValueError:
            print(f"\nYou entered {count} integers. Stopping input.")
            get_single_key("Press any key to continue...")
            break
    return numbers

def get_bunch_floats(numbers, n=None):
    """
    Reads floats from the user and appends them to the given list 'numbers'.

    Parameters:
    - numbers (list): A list to which read floats will be appended.
    - n (int, optional): If provided, the function reads exactly 'n' floats.
                         If not provided or None, it reads floats until a non-float is entered.

    Behavior:
    - Prompts the user to enter each float individually.
    - For fixed input count (n is given): continues until 'n' floats are entered or
      user enters a non-float.
    - For open-ended input (n is None): continues until a non-float is entered.
    - Displays a user-friendly prompt and clears the screen between inputs.

    Returns:
    - list: The updated list 'numbers' containing the floats entered by the user.
    """
    count = 0
    while True:
        clear_screen()
        if n is not None:
            print(f"Enter float number {count + 1} of {n} (or anything else to cancel):")
        else:
            print(f"Enter float number {count + 1} (or anything else to stop):")

        entry = input(">> ")
        try:
            number = float(entry)
            numbers.append(number)
            count += 1
            if n is not None and count >= n:
                break
        except ValueError:
            print("\nNon-float input detected. Stopping input.")
            break
    return numbers

def get_bunch_complex(num_values=1, message="Enter a complex number (a + bj): "):
    """
    Prompt the user for multiple complex numbers.

    Parameters:
    -----------
    num_values : int
        Number of complex numbers to read
    message : str, optional
        Custom prompt message to display to the user

    Returns:
    --------
    list
        List of complex numbers entered by the user
    """
    if num_values < 1:
        raise ValueError("Number of values must be at least 1")

    values = []
    count = 0

    while count < num_values:
        try:
            prompt = f"{message} [{count+1}/{num_values}]: "
            value = input(prompt).strip().replace(" ", "")

            # Handle input without imaginary part
            if 'j' not in value:
                complex_value = complex(float(value), 0)
            else:
                complex_value = complex(value)

            values.append(complex_value)
            count += 1

        except ValueError:
            print("Invalid input. Please enter a complex number in the form a+bj")
            print("Examples: 3+4j, 1-2j, 5 (for real numbers)")
            continue

    return values