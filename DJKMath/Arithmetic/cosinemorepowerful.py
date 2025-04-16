"""
The program computes the cosine of an angle using a power series expansion.
It allows the user to input the angle in either degrees or radians.
It also describes entered angles together with the converted degree/radian and its cosine.
Also, it compares the so computed cosine with the built-in cosine function.
It uses the mpmath library to compute the cosine with arbitrary precision,
which is more powerful than math library.
"""

import sys
import os
import mpmath  # Import for arbitrary precision computations

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
    """Gets a single-character input ('d' for degrees, 'r' for radians) without requiring Enter."""
    if os.name == "nt":
        while True:
            print("Enter 'd' for degree or 'r' for radian: ", end="", flush=True)
            choice = msvcrt.getch().decode().lower()
            if choice in ('d', 'r'):
                print(choice)
                return choice
            print("\nInvalid input. Please enter 'd' or 'r' only.")
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            while True:
                print("Enter 'd' for degree or 'r' for radian: ", end="", flush=True)
                tty.setraw(fd)
                choice = sys.stdin.read(1).lower()
                if choice in ('d', 'r'):
                    print(choice)
                    return choice
                print("\nInvalid input. Please enter 'd' or 'r' only.")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


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

            radian = mpmath.radians(degrees + minutes / 60 + seconds / 3600)
            radian = mpmath.fmod(radian, 2 * mpmath.pi)
            return radian, f"{degrees}° {minutes}' {seconds}\""
        except ValueError:
            print("Invalid input. Please enter integers only.")


def get_radian_input():
    """Gets a valid radian input from the user."""
    while True:
        try:
            radian = mpmath.mpf(input("Enter radians: "))
            radian = mpmath.fmod(radian, 2 * mpmath.pi)
            return radian, f"{mpmath.nstr(radian, 9)} rad"
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


def cosine_power_series(x, sig_digits):
    """Compute cos(x) using power series with range reduction and symmetry handling."""
    mpmath.mp.dps = sig_digits + 5
    pi = mpmath.pi
    x = mpmath.fmod(x, 2 * pi)

    # Reduce to [-π, π]
    if x > pi:
        x -= 2 * pi
    elif x < -pi:
        x += 2 * pi

    # Symmetry: cos(x) = cos(-x), cos(π - x) = -cos(x)
    sign = 1
    if x < 0:
        x = -x
    if x > pi / 2:
        x = pi - x
        sign = -1

    # Power series computation
    term = mpmath.mpf(1)
    cos_x = term
    n = 1
    x2 = x * x

    while abs(term) > mpmath.mpf(10) ** (-sig_digits):
        term *= -x2 / ((2 * n - 1) * (2 * n))
        cos_x += term
        n += 1

    return sign * +cos_x


def main():
    """Main function to execute the cosine calculation process."""
    choice = get_choice()

    if choice == 'd':
        radian, original_input = get_degree_input()
    else:
        radian, original_input = get_radian_input()

    degree_equivalent = mpmath.degrees(radian)
    sig_digits = get_significant_digits()

    cos_series = cosine_power_series(radian, sig_digits)
    cos_builtin = mpmath.cos(radian)

    print("\nResults:")
    print(f"Input given: {original_input}")
    print(f"Equivalent in degrees: {mpmath.nstr(degree_equivalent, 9)}°")
    print(f"Equivalent in radians: {mpmath.nstr(radian, 9)} rad")
    print("Computed cosine using power series           :", mpmath.nstr(cos_series, sig_digits))
    print("Cosine using high-precision built-in function:", mpmath.nstr(cos_builtin, sig_digits))
    print("Difference:", mpmath.nstr(abs(cos_series - cos_builtin), sig_digits))


if __name__ == "__main__":
    main()
    # This script is designed to be run directly.
