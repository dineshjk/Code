"""
This code demonstrates how to clear the console screen and print the rupee symbol in Python.
"""
print("\033c", end="")  # Clears the screen

items = ["apple", "banana", "cherry"]
price = [4, 8, 11]

for fruit, value in zip(items, price):
    print(f"Price of {fruit} is \u20b9 {value:.2f}")
print("\n")
