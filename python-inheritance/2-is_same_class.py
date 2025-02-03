#!/usr/bin/python3
"""Module to check if object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a class"""
    return type(obj) is a_class
