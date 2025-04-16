"""
trigo_sin_cos_tan.py
Main entry point for the high-precision trigonometric calculator using mpmath.
"""
import os
import sys

from mpmath import mp, mpf, radians, degrees, fmod, sin, cos, tan, inf



#sys.path.append(".")
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# According to many help files the least preferred and volatile is first one.
# The second is robust
# The third is the most robust and preferred.

from Utils import operate_menu, get_single_key, get_integer, get_float, wait_for_key



# from math_utils import *


def sine_power_series(x, precision):
    """Computes sine using Taylor series expansion around 0."""
    try:
        mp.dps = precision
        result = mpf(0)
        term = x
        n = 1
        total_terms = 1
        threshold = mpf(10) ** (-precision)

        while abs(term) > threshold:
            result += term
            n += 2
            term *= -(x**2) / (n * (n - 1))
            total_terms += 1
            if total_terms > 1000:  # Prevent infinite loops
                raise RuntimeError("Series not converging")
        return result, total_terms
    except (ValueError, RuntimeError) as e:
        print(f"Error in sine calculation: {e}")
        return mpf(0), 0

def cosine_power_series(x, precision):
    """Computes cosine using Taylor series expansion around 0."""
    try:
        mp.dps = precision
        result = mpf(1)
        term = mpf(1)
        n = 0
        total_terms = 1
        threshold = mpf(10) ** (-precision)

        while abs(term) > threshold:
            n += 2
            term *= -(x**2) / (n * (n - 1))
            result += term
            total_terms += 1
            if total_terms > 1000:  # Prevent infinite loops
                raise RuntimeError("Series not converging")
        return result, total_terms
    except (ValueError, RuntimeError) as e:
        print(f"Error in cosine calculation: {e}")
        return mpf(1), 0


def tangent_power_series(x, precision):
    """Computes tangent by invoking sine and cosine power series."""
    k = round((2 * x) / mp.pi)
    if k % 2 != 0:  # odd multiple
        expected = (k * mp.pi) / 2
        if abs(x - expected) < mpf(10) ** (
            -precision + 5
        ):  # within precision threshold
            print(
                f"\nTangent is undefined at this angle ({degrees(x)} degrees ≈ {k}·π/2)."
            )
            wait_for_key()
            result, terms_sine, terms_cos = "undefined", 0, 0
            return result, terms_sine, terms_cos
    sin_val, sin_terms = sine_power_series(x, precision)
    cos_val, cos_terms = cosine_power_series(x, precision)
    return sin_val / cos_val, sin_terms, cos_terms


def secant_power_series(x, precision):
    """Computes secant by taking the reciprocal of cosine power series."""
    k = round((2 * x) / mp.pi)
    if k % 2 != 0:  # odd multiple
        expected = (k * mp.pi) / 2
        if abs(x - expected) < mpf(10) ** (-precision + 5):
            print(
                f"\nSecant is undefined at this angle ({degrees(x)} degrees ≈ {k}·π/2)."
            )
            wait_for_key()
            result, terms = "undefined", 0
            return result, terms
    cos_val, cos_terms = cosine_power_series(x, precision)
    return mpf(1) / cos_val, cos_terms


def cosecant_power_series(x, precision):
    """Computes cosecant by taking the reciprocal of sine power series."""
    k = round(x / mp.pi)
    if abs(x - k * mp.pi) < mpf(10) ** (-precision + 5):  # near multiple of π
        print(f"\nCosecant is undefined at this angle ({degrees(x)} degrees ≈ {k}·π).")
        wait_for_key()
        result, terms = "undefined", 0
        return result, terms
    sin_val, sin_terms = sine_power_series(x, precision)
    return mpf(1) / sin_val, sin_terms


def cotangent_power_series(x, precision):
    """Computes cotangent by taking the reciprocal of tangent power series."""
    k = round(x / mp.pi)
    if abs(x - k * mp.pi) < mpf(10) ** (-precision + 5):  # near multiple of π
        print(f"\nCotangent is undefined at this angle ({degrees(x)} degrees ≈ {k}·π).")
        wait_for_key()
        result, terms_sine, terms_cos = "undefined", 0, 0
        return result, terms_sine, terms_cos
    sin_val, sin_terms = sine_power_series(x, precision)
    cos_val, cos_terms = cosine_power_series(x, precision)
    return cos_val / sin_val, sin_terms, cos_terms


def process_degree(given_degree, given_minute, given_second):
    """Processes the degree input and converts it to radians."""
    decimal_degree = given_degree + given_minute / 60 + given_second / 3600
    equivalent_radian = radians(decimal_degree)
    # Normalize the degree to be within [0, 360]
    normal_degree = fmod(decimal_degree, 360)
    # Convert to radians
    normal_radian = radians(normal_degree)
    normal_minute = fmod(normal_degree, 1) * 60
    normal_second = fmod(normal_minute, 1) * 60
    normal_degree = int(normal_degree)
    normal_minute = int(normal_minute)
    print(f"Given angle in degrees: {given_degree}° {given_minute}' {given_second}\"")
    print(f"Converted to radians: {equivalent_radian} rad")
    print(f"Decimal degrees: {decimal_degree}°")
    print(f"Normalized degrees: {normal_degree}° {normal_minute}' {normal_second}\"")
    print(f"Normalized radians: {normal_radian} rad")
    return normal_radian


def process_radian(given_radian):
    """Processes the radian input and converts it to degrees."""
    decimal_degree = degrees(given_radian)
    # Normalize the radian to be within [0, 2π]
    normal_radian = fmod(given_radian, 2 * mp.pi)
    normal_degree = degrees(normal_radian)
    normal_minute = fmod(normal_degree, 1) * 60
    normal_second = fmod(normal_minute, 1) * 60
    normal_degree = int(normal_degree)
    normal_minute = int(normal_minute)
    print(f"Given angle in radians: {given_radian} rad")
    print(f"Converted to degrees: {decimal_degree}°")
    print(f"Normalized degrees: {normal_degree}° {normal_minute}' {normal_second}\"")
    print(f"Normalized radians: {normal_radian} rad")
    return normal_radian


def get_precision():
    """Prompts the user for precision."""
    while True:
        try:
            precision = int(input("Enter precision (positive integer): ").strip())
            if 1 <= precision <= 1000:
                return precision
            else:
                print("Precision must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def flprint(value, precision, message=""):
    """Format and print the value with the specified precision."""
    mp.dps = precision  # Set display precision once
    print(
        f"{message} {mp.nstr(value, n=precision, strip_zeros=False, min_fixed=-inf, max_fixed=inf)}"
    )


def main():
    """Main function to run the trigonometric calculator."""
    menu_items = [
        ("[S] Sine", "S", "sine_power_series"),
        ("[C] Cosine", "C", "cosine_power_series"),
        ("[T] Tangent", "T", "tangent_power_series"),
        ("[E] Secant", "E", "secant_power_series"),
        ("[O] Cosecant", "O", "cosecant_power_series"),
        ("[N] Cotangent", "N", "cotangent_power_series"),
        ("[Q] Quit", "Q", "QUIT"),
    ]

    while True:
        # Step 1 Decide function.
        selected_func = operate_menu(menu_items)
        if selected_func is None:
            print("\nExiting...")
            break
        elif selected_func == "QUIT":
            print("\nExiting...")
            break
        # Step 2 Decide degree or radian.
        valid_keys = ["d", "r", "D", "R"]
        message = "Choose 'd' for degree or 'r' for radian: "
        dr = get_single_key(message, valid_keys)
        # Step 3 Get angle in degrees or radians.
        if dr == "D" or dr == "d":
            # Get angle in degrees
            origdr = "degree"
            # Get angle in degrees
            given_degree = get_integer("Enter angle in degrees: ")
            given_minute = get_integer("Enter minutes: ")
            given_second = get_float("Enter seconds: ")
            # Process degrees
            x = process_degree(given_degree, given_minute, given_second)
            # Convert to radians
        else:
            origdr = "radian"
            # Get angle in radians
            given_radian = get_float("Enter angle in radians: ")
            # Process radians
            x = process_radian(given_radian)
        # Step 4 Get precision.
        # Get precision
        precision = get_precision()
        # Step 5 Call the selected function.
        if selected_func == "sine_power_series":
            result, terms = sine_power_series(x, precision)
            builtin = sin(x)
            print("\nResults: ================")
            print(f"Function: {selected_func}")
            print(f"Angle given in {origdr}:")
            if origdr == "degree":
                process_degree(given_degree, given_minute, given_second)
            else:
                process_radian(given_radian)
            print(f"Precision: {precision} significant digits")
            print("\nSine Power Series Results:")
            mp.dps = precision  # Set display precision once
            print(f"Calculated Result: {result}")
            print(f"  Built-in Result: {builtin}")
            diff = abs(result - builtin)
            flprint(diff, precision, "       Difference: ")
            print(f"Number of terms used: {terms}")
        elif selected_func == "cosine_power_series":
            result, terms = cosine_power_series(x, precision)
            builtin = cos(x)
            print("\nResults: ================")
            print(f"Function: {selected_func}")
            print(f"Angle given in {origdr}:")
            if origdr == "degree":
                process_degree(given_degree, given_minute, given_second)
            else:
                process_radian(given_radian)
            print(f"Precision: {precision} significant digits")
            print("\nCosine Power Series Results:")
            mp.dps = precision  # Set display precision once
            print(f"Calculated Result: {mp.nstr(result, n=precision)}")
            print(f"  Built-in Result: {mp.nstr(builtin, n=precision)}")
            diff = abs(result - builtin)
            flprint(diff, precision, "       Difference: ")
            print(f"Number of terms used: {terms}")
        elif selected_func == "tangent_power_series":
            result, terms_sine, terms_cos = tangent_power_series(x, precision)
            if result == "undefined":
                print("Tangent is undefined.")
                builtin = "undefined"
            else:
                builtin = tan(x)
                print("\nResults: ================")
                print(f"Function: {selected_func}")
                print(f"Angle given in {origdr}:")
                if origdr == "degree":
                    process_degree(given_degree, given_minute, given_second)
                else:
                    process_radian(given_radian)
                print(f"Precision: {precision} significant digits")
                print("\nTangent Power Series Results:")
                mp.dps = precision  # Set display precision once
                print(f"Calculated Result: {mp.nstr(result, n=precision)}")
                print(f"  Built-in Result: {mp.nstr(builtin, n=precision)}")
                diff = abs(result - builtin)
                flprint(diff, precision, "       Difference: ")
                print(f"Number of terms used in sine: {terms_sine}")
                print(f"Number of terms used in cosine: {terms_cos}")
                print(f"Total terms used: {terms_sine + terms_cos}")
        elif selected_func == "secant_power_series":
            result, terms = secant_power_series(x, precision)
            if result == "undefined":
                print("Secant is undefined.")
                builtin = "undefined"
            else:
                builtin = mpf(1) / cos(x)
                diff = abs(result - builtin)
                if origdr == "degree":
                    process_degree(given_degree, given_minute, given_second)
                else:
                    process_radian(given_radian)
                print(f"Precision: {precision} significant digits")
                print("\nSecant Power Series Results:")
                mp.dps = precision  # Set display precision once
                print(f"Calculated Result: {mp.nstr(result, n=precision)}")
                print(f"  Built-in Result: {mp.nstr(builtin, n=precision)}")
                diff = abs(result - builtin)
                flprint(diff, precision, "       Difference: ")
                print(f"Number of terms used: {terms}")
        elif selected_func == "cosecant_power_series":
            result, terms = cosecant_power_series(x, precision)
            if result == "undefined":
                print("Cosecant is undefined.")
                builtin = "undefined"
            else:
                builtin = mpf(1) / sin(x)
                print("\nResults: ================")
                print(f"Function: {selected_func}")
                print(f"Angle given in {origdr}:")
                if origdr == "degree":
                    process_degree(given_degree, given_minute, given_second)
                else:
                    process_radian(given_radian)
                print(f"Precision: {precision} significant digits")
                print("\nCosecant Power Series Results:")
                mp.dps = precision  # Set display precision once
                print(f"Calculated Result: {mp.nstr(result, n=precision)}")
                print(f"  Built-in Result: {mp.nstr(builtin, n=precision)}")
                diff = abs(result - builtin)
                flprint(diff, precision, "       Difference: ")
                print(f"Number of terms used: {terms}")

        elif selected_func == "cotangent_power_series":
            result, terms_sine, terms_cos = cotangent_power_series(x, precision)
            if result == "undefined":
                print("Cotangent is undefined.")
                builtin = "undefined"
            else:
                builtin = cos(x) / sin(x)
                print("\nResults: ================")
                print(f"Function: {selected_func}")
                print(f"Angle given in {origdr}:")
                if origdr == "degree":
                    process_degree(given_degree, given_minute, given_second)
                else:
                    process_radian(given_radian)
                print(f"Precision: {precision} significant digits")
                print("\nCotangent Power Series Results:")
                mp.dps = precision  # Set display precision once
                print(f"Calculated Result: {mp.nstr(result, n=precision)}")
                print(f"  Built-in Result: {mp.nstr(builtin, n=precision)}")
                diff = abs(result - builtin)
                flprint(diff, precision, "       Difference: ")
                print(f"Number of terms used in sine: {terms_sine}")
                print(f"Number of terms used in cosine: {terms_cos}")
                print(f"Total terms used: {terms_sine + terms_cos}")
        get_single_key("\nPress a key to return to menu...")


if __name__ == "__main__":
    main()
