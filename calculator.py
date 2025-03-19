# calculator.py

# This module provides basic arithmetic operations.

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference when b is subtracted from a."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def round_to_places(num, places):
    """Return the number rounded to the specified number of decimal places."""
    return round(num, places)
