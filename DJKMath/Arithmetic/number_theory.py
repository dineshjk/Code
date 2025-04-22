D"""
number_theory.py
This script cotains functions for number theoretic computations
"""
import sys
import os
import msvcrt
from functools import reduce
# from Utils.keyboard_utils import get_single_key

# Add parent directory to Python path to find Utils package
#sys.path.append(".")
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# According to many help files the least preferred and volatile is first one.
# The second is robust
# The third is the most robust and preferred.

from Utils import clear_screen, get_single_key, get_integer, get_bunch_integers



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
    for i in range(1, n + 1):
        #print(f"Checking {i} ... ", end='\r')
        if n % i == 0:
            divisors.append(i)
            divisors.append(-i)
            tot_div += 2
    if return_count_only:
        return tot_div
    divisors.sort()
    return divisors, tot_div

def is_prime(n):
    """Check if a number n is prime."""
    if n < 0:
        n = -n
    if n < 2:
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
    if a*b == 0:
        return None
    while b:
        a, b = b, a % b
    return abs(a)

def lcm_two_numbers(a, b):
    """Calculate the least common multiple of a and b."""
    if a*b == 0:
        return None
    return abs(a * b) // gcd_two_numbers(a, b)

def lcm_numbers(numbers):
    """Calculate the least common multiple of multiple numbers."""
    return reduce(lcm_two_numbers, numbers)

def gcd_numbers(numbers):
    """Calculate the greatest common divisor of multiple numbers."""
    return reduce(gcd_two_numbers, numbers)


def is_coprime(a, b):
    """Check if two numbers a and b are coprime."""
    if a*b == 0:
        return False
    return gcd_two_numbers(a, b) == 1

def factorial(n):
    """Calculate the factorial of a number n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_first_n(n):
    """Generate Fibonacci numbers up to n."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    fib_numbers = [0, 1]
    no_of_terms = 2
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    while True:
        no_of_terms += 1
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > n:
            break
        fib_numbers.append(next_fib)
    return fib_numbers

def fibonacci_up_to_n(n):
    """Generate Fibonacci numbers up to n."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    fib_numbers = [0, 1]
    no_of_terms = 2
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    while True:
        no_of_terms += 1
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > n:
            break
        fib_numbers.append(next_fib)
    return fib_numbers

def ncr(n, r):
    """Calculate the binomial coefficient C(n, r)."""
    if r < 0 or r > n:
        raise ValueError("Invalid values for n and r.")
    if r == 0 or r == n:
        return 1
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    return numerator // denominator

def npr(n, r):
    """Calculate the number of permutations P(n, r)."""
    if r < 0 or r > n:
        raise ValueError("Invalid values for n and r.")
    if r == 0:
        return 1
    numerator = factorial(n)
    denominator = factorial(n - r)
    return numerator // denominator

def prime_factorization(n):
    """Calculate the prime factorization of a number n."""
    if n < 0:
        n = -n
    if n == 0:
        return {}
    if n == 1:
        return {1: 1}
    factors = {}
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
    if n > 1:
        factors[n] = 1
    return factors

def prime_factorization_list(n):
    """Calculate the prime factorization of a number n and return it as a list."""
    if n < 0:
        n = -n
    if n == 0:
        return []
    if n == 1:
        return [1]
    factors = []
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors











