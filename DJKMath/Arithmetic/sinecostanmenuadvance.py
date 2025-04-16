"""
This program computes sine, cosine, and tangent using power series.
It accepts angles in degrees or radians and compares the computed
result with the built-in mpmath function. Users can navigate
using arrow keys and hotkeys (S, C, T, Q).
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
        print("This script requires the tty and termios modules, "
              "which are not available on this platform.")
        sys.exit(1)

def get_single_key(prompt, valid_keys):
    """
    Wait for a keypress until a valid key from valid_keys is pressed.
    """
    valid_keys = {k.lower() for k in valid_keys}
    if os.name == "nt":
        while True:
            print(prompt, end="", flush=True)
            key = msvcrt.getch()
            if key in (b"\x00", b"\xe0"):
                msvcrt.getch()  # skip special key
                continue
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
    """Pause and wait for user to press any key to continue."""
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
    """Prompt user for degrees, minutes, seconds and return radians."""
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
    """Prompt user to enter radians and reduce within [0, 2π)."""
    while True:
        try:
            rad = mpmath.mpf(input("Enter radians: "))
            rad = mpmath.fmod(rad, 2 * mpmath.pi)
            return rad, f"{mpmath.nstr(rad, 7)} rad"
        except ValueError:
            print("Invalid input. Enter a valid number.")

def get_significant_digits():
    """Prompt user to enter the number of significant digits."""
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
    """Compute cosine using power series with optimizations."""
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
    while abs(term) > mpmath.mpf(10) ** (-sig_digits):
        term *= -x2 / ((2 * n - 1) * (2 * n))
        cos_x += term
        n += 1
    return sign * +cos_x, n

def sine_power_series(x, sig_digits):
    """Compute sine using power series with optimizations."""
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
    while abs(term) > mpmath.mpf(10) ** (-sig_digits):
        term *= -x2 / ((2 * n) * (2 * n + 1))
        sin_x += term
        n += 1
    return sign * +sin_x, n

def tangent_power_series(x, sig_digits):
    """Compute tangent using sine and cosine power series."""
    sin_x, terms1 = sine_power_series(x, sig_digits + 5)
    cos_x, terms2 = cosine_power_series(x, sig_digits + 5)
    if abs(cos_x) < mpmath.mpf(10) ** (-sig_digits):
        raise ZeroDivisionError("Tangent undefined.")
    return +(sin_x / cos_x), max(terms1, terms2)

def compute_and_display(name, compute_func):
    """Run selected trigonometric function with user input."""
    print(f"\nInitiating computation of {name.upper()} using power series.")
    while True:
        choice = get_single_key(
            "Enter 'd' or 'D' for degree or 'r' or 'R' for radian: ", "drDR")
        print(choice)
        if choice.lower() == 'd':
            radian, original = get_degree_input()
            break
        elif choice.lower() == 'r':
            radian, original = get_radian_input()
            break
    sig_digits = get_significant_digits()
    result, terms_used = compute_func(radian, sig_digits)
    builtin = getattr(mpmath, name)(radian)
    print("\nResults:")
    print(f"Input given: {original}")
    print("Equivalent in degrees:",
          mpmath.nstr(mpmath.degrees(radian), 10) + "°")
    print("Equivalent in radians:", mpmath.nstr(radian, 10) + " rad")
    print(f"Computed {name} using power series:",
          mpmath.nstr(result, sig_digits))
    print(f"Built-in high-precision {name} function:",
          mpmath.nstr(builtin, sig_digits))
    print("Difference:", mpmath.nstr(abs(result - builtin), sig_digits))
    print(f"Terms used in {name} series: {terms_used}")
    wait_for_key()

def main():
    """Start the interactive trigonometric calculator."""
    menu()

from menu_logic import menu
