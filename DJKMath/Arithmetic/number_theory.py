"""
all_divisors.py
This script calculates all divisors of a given number.

"""
import sys
# import os
from functools import reduce

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

sys.path.append(".")

from math import sqrt
from Utils import clear_screen
from Utils import get_integer



def all_divisors(n, return_count_only=False):
    """Calculate all divisors of a given number n."""
    divisors = []
    tot_div = 0
    if n == 0:
        return 0 if return_count_only else (divisors, 0)
    if n < 0:
        n = -n
    if n == 1:
        return 2 if return_count_only else ([1, -1], 2)
    for i in range(1, int(sqrt(n)) + 1):
        print(f"Checking divisor: {i}")
        if n % i == 0:
            divisors.append(i)
            divisors.append(-i)
            tot_div += 2
            print(f"Divisor found: {i} and {-i}")
    if return_count_only:
        return tot_div
    divisors.sort()
    return divisors, tot_div

def is_prime(n):
    """Check if a number n is prime."""
    if n < 0:
        n = -n
    elif n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def gcd_two_numbers(a, b):
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm_two_numbers(a, b):
    """Calculate the least common multiple of a and b."""
    return abs(a * b) // gcd_two_numbers(a, b)

def lcm_numbers(numbers):
    """Calculate the least common multiple of multiple numbers."""
    return reduce(lcm_two_numbers, numbers)

def gcd_numbers(numbers):
    """Calculate the greatest common divisor of multiple numbers."""
    return reduce(gcd_two_numbers, numbers)



def main():
    """Main function to find all divisors of a number."""
    clear_screen()
    n = get_integer("Give Integer number to find all divisors: ")
    divisors, no_of_div = all_divisors(n)
    print(f"All the {no_of_div} factors of {n} are: {divisors}")

    if is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

if __name__ == "__main__":
    main()
