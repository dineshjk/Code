"""
This program computes sine, cosine, and tangent using power series.
It allows the user to input angles in degrees, minutes, and seconds or
in radians. Results are compared with the built-in high-precision
functions from the mpmath library. A menu lets the user choose a
function using arrow keys or hotkeys (s, c, t, q). The program also
shows how many terms were used in the power series.
"""

import os
import sys
import mpmath

if os.name == "nt":
    import msvcrt
else:
    try:
        import tty
        import termios
    except ImportError:
        print("This script requires tty and termios modules, which are "
              "not available on this platform.")
        sys.exit(1)

def get_single_key(prompt, valid_keys):
    """
    Prompt the user with a message and wait for a valid key press.
    Only keys in valid_keys are accepted.
    """
    valid_keys = {k.lower() for k in valid_keys}
    if os.name == "nt":
        while True:
            print(prompt, end="", flush=True)
            key = msvcrt.getch()
            try:
                key = key.decode().lower()
            except UnicodeDecodeError:
                continue
            if key in valid_keys:
                print(key)
                return key
            print("\nInvalid input.")
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            while True:
                print(prompt, end="", flush=True)
                tty.setraw(fd)
                key = sys.stdin.read(1).lower()
                if key in valid_keys:
                    print(key)
                    return key
                print("\nInvalid input.")
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def wait_for_key():
    """
    Display 'Press any key to continue...' and wait for any key.
    """
    print("\nPress any key to continue...", end="", flush=True)
    if os.name == "nt":
        msvcrt.getch()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def get_degree_input():
    """
    Prompt the user to enter angle in degrees, minutes, and seconds.
    Returns angle in radians and formatted string.
    """
    while True:
        try:
            deg = int(input("Enter degrees (0-360): "))
            min_ = int(input("Enter minutes (0-60): "))
            sec = int(input("Enter seconds (0-60): "))

            if not (0 <= deg <= 360 and 0 <= min_ < 60 and 0 <= sec < 60):
                print("Invalid input. Check ranges.")
                continue

            total_deg = deg + min_ / 60 + sec / 3600
            rad = mpmath.radians(total_deg) % (2 * mpmath.pi)
            return rad, f"{deg}° {min_}' {sec}\""
        except ValueError:
            print("Invalid input. Enter integers only.")

def get_radian_input():
    """
    Prompt the user to enter angle in radians. Returns angle in
    radians and formatted string.
    """
    while True:
        try:
            rad = mpmath.mpf(input("Enter radians: "))
            rad = mpmath.fmod(rad, 2 * mpmath.pi)
            return rad, f"{mpmath.nstr(rad, 7)} rad"
        except ValueError:
            print("Invalid input. Enter a valid number.")

def get_significant_digits():
    """
    Prompt the user to enter the number of significant digits.
    Must be a positive integer.
    """
    while True:
        try:
            digits = int(input("Enter the number of significant digits: "))
            if digits > 0:
                return digits
            else:
                print("Enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a valid integer.")

def cosine_power_series(x, sig_digits):
    """
    Compute cosine of x using power series with angle reduction.
    """
    mpmath.mp.dps = sig_digits + 5
    pi = mpmath.pi
    x = mpmath.fmod(x, 2 * pi)

    if x > pi:
        x -= 2 * pi
    elif x < -pi:
        x += 2 * pi

    sign = 1
    if x < 0:
        x = -x
    if x > pi / 2:
        x = pi - x
        sign = -1

    term = mpmath.mpf(1)
    cos_x = term
    n = 1
    x2 = x * x
    terms_used = 1

    while abs(term) > mpmath.mpf(10) ** (-sig_digits):
        term *= -x2 / ((2 * n - 1) * (2 * n))
        cos_x += term
        n += 1
        terms_used += 1

    print(f"Terms used in cos series: {terms_used}")
    return sign * +cos_x

def sine_power_series(x, sig_digits):
    """
    Compute sine of x using power series with angle reduction.
    """
    mpmath.mp.dps = sig_digits + 5
    pi = mpmath.pi
    x = mpmath.fmod(x, 2 * pi)

    if x > pi:
        x -= 2 * pi
    elif x < -pi:
        x += 2 * pi

    sign = 1
    if x < 0:
        x = -x
        sign = -1

    term = x
    sin_x = term
    n = 1
    x2 = x * x
    terms_used = 1

    while abs(term) > mpmath.mpf(10) ** (-sig_digits):
        term *= -x2 / ((2 * n) * (2 * n + 1))
        sin_x += term
        n += 1
        terms_used += 1

    print(f"Terms used in sin series: {terms_used}")
    return sign * +sin_x

def tangent_power_series(x, sig_digits):
    """
    Compute tangent of x using sin(x)/cos(x) with series for each.
    """
    sin_x = sine_power_series(x, sig_digits + 5)
    cos_x = cosine_power_series(x, sig_digits + 5)
    if abs(cos_x) < mpmath.mpf(10) ** (-sig_digits):
        raise ZeroDivisionError("Tangent undefined: cosine near zero.")
    return + (sin_x / cos_x)

def compute_and_display(func_name, compute_func):
    """
    Run the chosen computation. Ask user for angle and precision.
    Show computed result, built-in value, and difference.
    """
    while True:
        choice = get_single_key(
            "Enter 'd' for degree or 'r' for radian: ", "drDR")
        choice = choice.lower()
        if choice in ('d', 'r'):
            break

    if choice == 'd':
        radian, original = get_degree_input()
    else:
        radian, original = get_radian_input()

    sig_digits = get_significant_digits()
    result = compute_func(radian, sig_digits)
    builtin = getattr(mpmath, func_name)(radian)

    print("\nResults:")
    print(f"Input given: {original}")
    print("Equivalent in degrees:",
          mpmath.nstr(mpmath.degrees(radian), 10) + "°")
    print("Equivalent in radians:",
          mpmath.nstr(radian, 10) + " rad")
    print(f"Computed {func_name} using power series:",
          mpmath.nstr(result, sig_digits))
    print(f"Built-in high-precision {func_name} function:",
          mpmath.nstr(builtin, sig_digits))
    print("Difference:", mpmath.nstr(abs(result - builtin), sig_digits))
    wait_for_key()

def main():
    """
    Show menu for user to choose sine, cosine, tangent, or quit.
    Use arrow keys or hotkeys to navigate and select an item.
    """
    menu_items = [
        ("Sine", 's', lambda: compute_and_display("sin",
                                                  sine_power_series)),
        ("Cosine", 'c', lambda: compute_and_display("cos",
                                                    cosine_power_series)),
        ("Tangent", 't', lambda: compute_and_display("tan",
                                                     tangent_power_series)),
        ("Quit", 'q', lambda: sys.exit("Exiting program."))
    ]

    index = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Choose a function to compute using power series:")
        for i, (label, key, _) in enumerate(menu_items):
            prefix = "-->" if i == index else "   "
            print(f"{prefix} [{key.upper()}] {label}")

        if os.name == 'nt':
            key = msvcrt.getch()
            if key in (b'\xe0', b'\x00'):
                key = msvcrt.getch()
                if key == b'H':
                    index = (index - 1) % len(menu_items)
                    continue
                elif key == b'P':
                    index = (index + 1) % len(menu_items)
                    continue
            else:
                try:
                    key = key.decode().lower()
                except UnicodeDecodeError:
                    continue
        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setraw(fd)
            key = sys.stdin.read(1)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            key = key.lower()

        if key == '\r' or key == '\n':
            label, k, func = menu_items[index]
            print(f"\nInitiating computation of {label.upper()} using "
                  "power series.")
            func()
        else:
            for i, (label, k, func) in enumerate(menu_items):
                if key == k:
                    print(f"\nInitiating computation of {label.upper()} using "
                          "power series.")
                    func()
                    break

if __name__ == "__main__":
    main()
