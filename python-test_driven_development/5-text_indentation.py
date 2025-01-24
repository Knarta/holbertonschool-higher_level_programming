#!/usr/bin/python3
"""
Module to print a text with 2 new lines after
each of these characters: ., ? and :
the function prints the text with the new lines
"""


def text_indentation(text):
    """
    Function to print a text with 2 new
    lines after each of these characters: ., ? and :
    return: None
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    i = 0
    res = ""

    while i < len(text):
        res += text[i]
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            res += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(res, end="")
