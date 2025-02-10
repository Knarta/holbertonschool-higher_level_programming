#!/usr/bin/python3
"""
Read a text file (UTF8) and print it to stdout
"""


def read_file(filename="my_file_0.txt"):
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
