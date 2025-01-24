#!/usr/bin/python3
"""
Module to add two integers
a and b must be integers or floats
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    Function to add two integers
    return: sum of two integers
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
