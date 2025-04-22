from Fraction import Fraction


if __name__ == "__main__":
    try:
        fraction1 = Fraction(*map(int, input("Enter the first fraction (e.g., 7/9 or -7/9): ").split('/')))
        fraction2 = Fraction(*map(int, input("Enter the second fraction (e.g., 7/9 or -7/9): ").split('/')))

        # Perform all operations
        result1 = fraction1 + fraction2
        result2 = fraction1 - fraction2
        result3 = fraction1 * fraction2
        result4 = fraction1 / fraction2

        # Display results
        print(f"\nResults for fractions {fraction1} and {fraction2}:")
        print(f"Addition:       {result1}")
        print(f"Subtraction:    {result2}")
        print(f"Multiplication: {result3}")
        print(f"Division:       {result4}")
        print(f"Equality:       {fraction1 == fraction2}")
        print(f"Less than:      {fraction1 < fraction2}")
        print(f"Less than or equal: {fraction1 <= fraction2}")
        print(f"Greater than:   {fraction1 > fraction2}")

    except ValueError as e:
        print("Error: Please enter fractions in the format 'n/d' where n and d are integers")
        print("Example: 7/9 or -7/9")