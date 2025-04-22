"""
Arithmetic/__init__.py
Expose commonly used utilities by default when importing from Utils.
"""
from .number_theory import (
    all_divisors,
    is_prime,
    gcd_two_numbers,
    lcm_two_numbers,
    lcm_numbers,
    gcd_numbers,
    is_coprime,
    factorial,
    fibonacci,
    fibonacci_first_n,
    fibonacci_up_to_n,
    ncr,
    npr,
    prime_factorization,
    prime_factorization_list
)

__all__ = [
    'all_divisors',
    'is_prime',
    'gcd_two_numbers',
    'lcm_two_numbers',
    'lcm_numbers',
    'gcd_numbers',
    'is_coprime',
    'factorial',
    'fibonacci',
    'fibonacci_first_n',
    'fibonacci_up_to_n',
    'ncr',
    'npr',
    'prime_factorization',
    'prime_factorization_list'
]
