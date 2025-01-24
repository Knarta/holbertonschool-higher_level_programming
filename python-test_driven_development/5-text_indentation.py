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
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    i = 0
    res = ""
    while i < len(text):
        res = text[i]
        if text[i] in [".", "?", ":"]:
            res += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(res, end="")
