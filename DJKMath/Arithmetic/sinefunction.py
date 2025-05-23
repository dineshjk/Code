"""
The program computes the sine of an angle using a power series expansion.
It allows the user to input the angle in either degrees or radians.
It also describes entered angles to gether with the converted degree/radian and its sine.
Also, it compares the so computed sine with the built-in sine function.
"""
import math
import sys
import os

# Platform-specific single-character input
if os.name == "nt":  # Windows system
    import msvcrt
else:
    try:
        import tty
        import termios
    except ImportError:
        print("""This script requires the tty
               and termios modules, which are not available on
               this platform.""")
        sys.exit(1)
def get_choice():
    """Gets a single-character input ('d' for degrees, 'r' for radians) without requiring Enter.
    Keeps iterating until a valid input is provided."""
    if os.name == "nt":  # Windows system
        while True:
            print("Enter 'd' for degree or 'r' for radian: ", end="", flush=True)
            choice = msvcrt.getch().decode().lower()
            if choice in ('d', 'r'):
                print(choice)  # Show the chosen character
                return choice
            print("\nInvalid input. Please enter 'd' or 'r' only.")
    else:  # Unix-like systems (Linux, macOS)
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            while True:
                print("Enter 'd' for degree or 'r' for radian: ", end="", flush=True)
                tty.setraw(fd)
                choice = sys.stdin.read(1).lower()
                if choice in ('d', 'r'):
                    print(choice)  # Show the chosen character
                    return choice
                print("\nInvalid input. Please enter 'd' or 'r' only.")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def sine_power_series(x, sig_digits):
    """Computes sin(x) using power series expansion until the desired significant digits."""
    sin_x, term, n = 0, x, 1

    while abs(term) > 10 ** (-sig_digits):
        sin_x += term
        n += 2
        term *= -x ** 2 / (n * (n - 1))

    return sin_x

def normalize_radian(x):
    """Brings x in radians to the range [-pi, pi] using modulo operation."""
    return (x + math.pi) % (2 * math.pi) - math.pi

def get_degree_input():
    """Gets a valid degree, minutes, and seconds input from the user."""
    while True:
        try:
            degrees = int(input("Enter degrees (0-360): "))
            minutes = int(input("Enter minutes (0-60): "))
            seconds = int(input("Enter seconds (0-60): "))

            if not (0 <= degrees <= 360 and 0 <= minutes < 60 and 0 <= seconds < 60):
                print("Invalid input. Ensure degrees are 0-360, minutes 0-60, and seconds 0-60.")
                continue

            radian = math.radians(degrees + minutes / 60 + seconds / 3600)
            return radian, f"{degrees}° {minutes}' {seconds}\""
        except ValueError:
            print("Invalid input. Please enter integers only.")

def get_radian_input():
    """Gets a valid radian input from the user."""
    while True:
        try:
            radian = float(input("Enter radians: "))
            return radian, f"{radian:.6f} rad"
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_significant_digits():
    """Gets a valid positive integer for significant digits."""
    while True:
        try:
            sig_digits = int(input("Enter the number of significant digits: "))
            if sig_digits > 0:
                return sig_digits
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    """Main function to execute the sine calculation process."""
    choice = get_choice()

    if choice == 'd':
        radian, original_input = get_degree_input()
    else:
        radian, original_input = get_radian_input()

    radian = normalize_radian(radian)
    degree_equivalent = math.degrees(radian)

    sig_digits = get_significant_digits()

    sin_series = sine_power_series(radian, sig_digits)
    sin_builtin = math.sin(radian)

    print("\nResults:")
    print(f"Input given: {original_input}")
    print(f"Equivalent in degrees: {degree_equivalent:.6f}°")
    print(f"Equivalent in radians: {radian:.6f} rad")
    print(f"Computed sine using power series: {sin_series:.{sig_digits}f}")
    print(f"Sine using built-in function    : {sin_builtin:.{sig_digits}f}")
    print(f"Difference: {abs(sin_series - sin_builtin):.{sig_digits}e}")
    print(f"Difference: {abs(sin_series - sin_builtin):.{sig_digits}f}")


if __name__ == "__main__":
    main()
