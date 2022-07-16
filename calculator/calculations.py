# calculator/calculations.py

"""Provide several simple math calculations.

This module allows the user to make mathematical calculations.

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""
from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of 'a' and 'b'.
    """
    return float(a + b)


def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the difference between two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a: a number representing the first term in the subtraction.
        b: a number representing the second term in the subtraction.

    Returns:
        A number representing the arithmetic difference between 'a' and 'b'.
    """
    return float(a - b)


def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: a number representing the first term in the multiplication.
        b: a number representing the second term in the multiplication.

    Returns:
        A number representing the product of the two terms.
    """
    return float(a * b)


def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the quotient of a dividend and a divisor.

    Examples:
        >>> divide(12.0, 2.0)
        6.0
        >>> divide(12, 2)
        6.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

    Args:
        a (float): a number representing the dividend.
        b (float): a number representing the divisor.

    Returns:
        float: a number representing the quotient of the dividend and the divisor.

    Raises:
        ZeroDivisionError: An error occurs when the divisor is '0'.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
