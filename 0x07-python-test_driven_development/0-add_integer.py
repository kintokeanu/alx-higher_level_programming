#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either `a` or `b` is not an integer.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
