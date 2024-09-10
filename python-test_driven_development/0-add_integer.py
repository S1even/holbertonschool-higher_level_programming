#!/usr/bin/python3
"""
This function to add two integers
"""

def add_integer(a, b=98):
    """
    Adds two integers :
    a: the first number
    b: the second number, deefaults to 98

    Returns:
    the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
