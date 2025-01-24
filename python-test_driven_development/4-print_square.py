#!/usr/bin/python3
"""
Module to print a square
the function prints a square with the character #
"""


def print_square(size):
    """
    Function to print a square
    return: None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
