#!/usr/bin/python3

"""
Module to write a file with a given text
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as my_first_file:
        my_first_file.write(text)
        return len(text)
