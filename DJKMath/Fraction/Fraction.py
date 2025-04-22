from math import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer.")
        self.numerator = numerator
        self.denominator = denominator
        self.normalize()

    def normalize(self):
        """Normalize the fraction by cancelling common factors."""
        common_factor = gcd(self.numerator, self.denominator)
        self.numerator //= common_factor
        self.denominator //= common_factor
        if self.denominator < 0:  # Ensure denominator is always positive
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @staticmethod
    def from_string(fraction_str: str):
        """Read a fraction from a string in the form a/b."""
        numerator, denominator = map(int, fraction_str.split('/'))
        return Fraction(numerator, denominator)

    def __add__(self, other):
        """Add two fractions or a fraction and an integer."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Subtract two fractions or a fraction and an integer."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Multiply two fractions or a fraction and an integer."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """Divide two fractions or a fraction and an integer."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """Compare if two fractions are equal."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        """Compare if this fraction is less than another."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        """Compare if this fraction is less than or equal to another."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __str__(self):
        """Print the fraction in the form a/b."""
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """Representation of the fraction."""
        return f"Fraction({self.numerator}, {self.denominator})"