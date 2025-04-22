"""The module contains functions to compute sine, cosine, and tangent using power series."""


from mpmath import mp, mpf, radians, degrees, fmod, sin, cos, tan
from keyboard_input import get_single_key
from keyboard_utils import clear_screen, wait_for_key


def sine_power_series(x, precision):
    """Computes sine using Taylor series expansion around 0."""
    mp.dps = precision
    result = mpf(0)
    term = x
    n = 1
    total_terms = 1
    while abs(term) > mpf(10) ** (-precision):
        result += term
        n += 2
        term *= -(x**2) / (n * (n - 1))
        total_terms += 1
    return result, total_terms


def cosine_power_series(x, precision):
    """Computes cosine using Taylor series expansion around 0."""
    mp.dps = precision
    result = mpf(1)
    term = mpf(1)
    n = 0
    total_terms = 1
    while abs(term) > mpf(10) ** (-precision):
        n += 2
        term *= -(x**2) / (n * (n - 1))
        result += term
        total_terms += 1
    return result, total_terms


def tangent_power_series(x, precision):
    """Computes tangent by invoking sine and cosine power series."""
    sin_val, sin_terms = sine_power_series(x, precision)
    cos_val, cos_terms = cosine_power_series(x, precision)
    return sin_val / cos_val, sin_terms + cos_terms


def normalize_radian(x):
    """Normalizes angle to be within the range [-π, π]."""
    return fmod(x, 2 * mp.pi)


def compute_and_display(label, func_name):
    """Computes and displays the result of the trigonometric function."""
    clear_screen()
    print(f"\nInitiating computation of {label} using power series.")
    # Step 1: Get 'd' or 'r' from single key
    while True:
        print(
            "Enter 'd' or 'D' for degree or 'r' or 'R' for radian: ", end="", flush=True
        )
        key = get_single_key()
        print(key)
        if key.lower() in {"d", "r"}:
            break
        print("Invalid key. Please press only 'd', 'D', 'r', or 'R'.")

    # Step 2: Input angle
    if key.lower() == "d":
        origdr= "degrees"
        while True:
            try:
                deg = int(input("Enter degrees (integer): ").strip())
                break
            except ValueError:
                print("Invalid input. Please enter an integer for degrees.")
        while True:
            try:
                minutes = int(input("Enter minutes (integer): ").strip())
                break
            except ValueError:
                print("Invalid input. Please enter an integer for minutes.")
        while True:
            try:
                seconds = mpf(input("Enter seconds (float): ").strip())
                break
            except ValueError:
                print("Invalid input. Please enter a float for seconds.")
        decimal_deg = deg + minutes / 60 + seconds / 3600
        x = radians(decimal_deg)
    else:
        while True:
            try:
                origdr = "radians"
                x = mpf(input("Enter radians: ").strip())
                given_rad = x
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    x = normalize_radian(x)

    # Step 3: Precision
    while True:
        try:
            precision = int(
                input(
                    "Enter the number of significant digits "
                    "(positive integer): "
                ).strip()
            )
            if precision > 0:
                break
            else:
                print("Precision must be a positive integer.")
        except ValueError:
            print("Precision must be a positive integer.")

    # Step 4: Computation
    if func_name == "sine_power_series":
        result, terms = sine_power_series(x, precision)
        builtin = sin(x)
    elif func_name == "cosine_power_series":
        result, terms = cosine_power_series(x, precision)
        builtin = cos(x)
    elif func_name == "tangent_power_series":
        # Tangent is undefined at odd multiples of pi/2
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
                return
        result, terms = tangent_power_series(x, precision)
        builtin = tan(x)

    diff = abs(result - builtin)

    print("\n--- Result Summary ---")
    if origdr == "degrees":
        print(f"You gave D M C: {deg}° {minutes}' {seconds}\"")
    else:
        print(f"You gave R: {given_rad} radian")
    print(f"Radian (normalized): {x}")
    print(f"Degrees (equivalent): {degrees(x)}")
    print(f"Precision: {precision} digits")
    print(f"Computed {label}: {result}")
    print(f"Built-in {label}: {builtin}")
    print(f"Difference: {diff}")
    print(f"Total terms used: {terms}")

    wait_for_key()
    return 0
