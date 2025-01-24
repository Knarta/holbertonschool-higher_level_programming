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
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
