#!/usr/bin/python3
""" Module that defines a class Square """


class Square:
    """ Class that defines a square """
    __size = None

    def __init__(self, size=__size):
        if size is not None:
            self.__size = size
