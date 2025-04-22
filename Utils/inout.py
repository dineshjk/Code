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

from .keyboard_utils import clear_screen, get_single_key, wait_for_key

def get_integer(constraint=None, message="Enter an integer: ", range_min=None, range_max=None):
    """Prompt the user for an integer with optional constraints.

    Parameters:
    -----------
    constraint : str, optional
        Type of constraint to apply:
        - "positive": Only accept positive integers (> 0)
        - "negative": Only accept negative integers (< 0)
        - "non-negative": Only accept integers >= 0
        - "non-positive": Only accept integers <= 0
        - None: Accept any integer (default)
        Note: When constraint is specified, range_min and range_max must be None
    message : str, optional
        Custom prompt message to display to the user
    range_min : int, optional
        Minimum value (inclusive) for the integer input
        Must be None if constraint is specified
    range_max : int, optional
        Maximum value (inclusive) for the integer input
        Must be None if constraint is specified

    Returns:
    --------
    int
        The validated integer input that meets the specified constraint

    Raises:
    -------
    ValueError
        - If the input cannot be converted to an integer
        - If both constraint and range parameters are specified
        - If range_min > range_max
    KeyboardInterrupt
        If the user cancels the input (Ctrl+C)
    RuntimeError
        If an unexpected error occurs during input processing

    Examples:
    --------
    # Using constraints (no ranges allowed with constraints)
    >>> num = get_integer("positive")                 # Gets number > 0
    >>> num = get_integer("negative")                 # Gets number < 0
    >>> num = get_integer("non-negative")             # Gets number >= 0
    >>> num = get_integer("non-positive")             # Gets number <= 0

    # Using ranges (no constraints allowed with ranges)
    >>> num = get_integer(range_min=1, range_max=10)  # Gets number between 1 and 10
    >>> num = get_integer(range_min=0, range_max=100) # Gets number between 0 and 100
    >>> num = get_integer(range_min=-10, range_max=10)# Gets number between -10 and 10

    # Basic usage (no constraints or ranges)
    >>> num = get_integer()                           # Gets any integer
    >>> num = get_integer(message="Enter age: ")      # Gets any integer with custom message
    """
    # Validate constraint and range compatibility
    if constraint is not None and (range_min is not None or range_max is not None):
        raise ValueError("Cannot specify both constraint and range parameters")

    # Validate range constraints if provided
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
            if constraint == "non-negative" and value < 0:
                print("Please enter a non-negative integer (greater than or equal to 0).")
                continue
            if constraint == "non-positive" and value > 0:
                print("Please enter a non-positive integer (less than or equal to 0).")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter an integer only.")
            continue
        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
            raise KeyboardInterrupt("Input operation cancelled by user")
        except Exception as e:
            error_msg = f"Unexpected error during integer input: {str(e)}"
            print(error_msg)
            continue

def get_float(constraint=None, message="Enter a float: ", range_min=None, range_max=None):
    """Get float input from user with error handling and constraints.

    Parameters:
    -----------
    constraint : str, optional
        Type of constraint to apply:
        - "positive": Only accept positive numbers (> 0)
        - "negative": Only accept negative numbers (< 0)
        - "non-negative": Only accept numbers >= 0
        - "non-positive": Only accept numbers <= 0
        - None: Accept any float (default)
        Note: When constraint is specified, range_min and range_max must be None
    message : str, optional
        Custom prompt message to display to the user
    range_min : float, optional
        Minimum value (inclusive) for the float input
        Must be None if constraint is specified
    range_max : float, optional
        Maximum value (inclusive) for the float input
        Must be None if constraint is specified

    Returns:
    --------
    float
        The validated float value meeting specified constraints

    Raises:
    -------
    ValueError
        - If the input cannot be converted to a float
        - If both constraint and range parameters are specified
        - If range_min > range_max
    KeyboardInterrupt
        If the user cancels the input (Ctrl+C)
    RuntimeError
        If an unexpected error occurs during input processing

    Examples:
    --------
    # Using constraints (no ranges allowed with constraints)
    >>> num = get_float("positive")                 # Gets number > 0
    >>> num = get_float("negative")                 # Gets number < 0
    >>> num = get_float("non-negative")             # Gets number >= 0
    >>> num = get_float("non-positive")             # Gets number <= 0

    # Using ranges (no constraints allowed with ranges)
    >>> num = get_float(range_min=1, range_max=10)  # Gets number between 1 and 10
    >>> num = get_float(range_min=0, range_max=100) # Gets number between 0 and 100
    >>> num = get_float(range_min=-10, range_max=10)# Gets number between -10 and 10

    # Basic usage (no constraints or ranges)
    >>> num = get_float()                           # Gets any float
    >>> num = get_float(message="Enter pH: ")       # Gets any float with custom message
    """
    # Validate constraint and range compatibility
    if constraint is not None and (range_min is not None or range_max is not None):
        raise ValueError("Cannot specify both constraint and range parameters")

    # Validate range constraints if provided
    if range_min is not None and range_max is not None:
        if range_min > range_max:
            raise ValueError(f"Invalid range: min ({range_min}) cannot be greater than max ({range_max})")
        message = f"{message} [{range_min}-{range_max}]: "

    while True:
        try:
            value = float(input(message).strip())

            # Check range constraints
            if range_min is not None and value < range_min:
                print(f"Please enter a number greater than or equal to {range_min}.")
                continue
            if range_max is not None and value > range_max:
                print(f"Please enter a number less than or equal to {range_max}.")
                continue

            # Check other constraints
            if constraint == "positive" and value <= 0:
                print("Please enter a positive number (greater than 0).")
                continue
            if constraint == "negative" and value >= 0:
                print("Please enter a negative number (less than 0).")
                continue
            if constraint == "non-negative" and value < 0:
                print("Please enter a non-negative number (greater than or equal to 0).")
                continue
            if constraint == "non-positive" and value > 0:
                print("Please enter a non-positive number (less than or equal to 0).")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
            raise KeyboardInterrupt("Input operation cancelled by user")
        except Exception as e:
            error_msg = f"Unexpected error during float input: {str(e)}"
            print(error_msg)
            continue

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

    if n is not None:
        if n < 1:
            raise ValueError("Number of values must be at least 1")
        numbers.extend([0] * n)
        for i in range(n):
            while True:
                print(f"Enter integer number {i+1} of {n} ")
                entry = input(">> ")
                try:
                    numbers[i] = int(entry)
                    break
                except (ValueError, TypeError):
                    print(f"Invalid input for {i}th integer. Please enter an integer")
                    continue
        return numbers
    count = 0
    while True:
        print(f"Enter integer number {count+1} (or anything else to stop):")
        entry = input(">> ")
        try:
            number = int(entry)
            numbers.append(number)
            count += 1
        except ValueError:
            print(f"\nYou entered {count} integers. Stopping input.")
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

    if n is not None:
        if n < 1:
            raise ValueError("Number of values must be at least 1")
        numbers.extend([0] * n)
        for i in range(n):
            while True:
                print(f"Enter a real number {i+1} of {n} ")
                entry = input(">> ")
                try:
                    numbers[i] = float(entry)
                    break
                except (ValueError, TypeError):
                    print(f"Invalid input for {i}th integer. Please enter an integer")
                    continue
        return numbers
    count = 0
    while True:
        print(f"Enter a real number {count+1} (or anything else to stop):")
        entry = input(">> ")
        try:
            number = float(entry)
            numbers.append(number)
            count += 1
        except ValueError:
            print(f"\nYou entered {count} real numbers. Stopping input.")
            return numbers

def get_bunch_complex(values, num_values=None, message="Enter a complex number (a + bj): "):
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
    if num_values is not None:
        if num_values < 1:
            raise ValueError("Number of values must be at least 1")

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
    count = 0
    while True:
        try:
            prompt = f"{message} [{count+1}. Enter anything else to stop.]: "
            value = input(prompt).strip().replace(" ", "")

            # Handle input without imaginary part
            if 'j' not in value:
                complex_value = complex(float(value), 0)
            else:
                complex_value = complex(value)

            values.append(complex_value)
            count += 1

        except ValueError:
            print("You entered {count} complex numbers. Stopping input.")
            return values

        except KeyboardInterrupt:
            print("\nInput cancelled by user.")
            raise KeyboardInterrupt("Input operation cancelled by user")

        except Exception as e:
            error_msg = f"Unexpected error during complex input: {str(e)}"
            print(error_msg)
            raise RuntimeError("Unexpected error during complex input")