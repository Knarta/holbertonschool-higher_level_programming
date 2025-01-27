#!/usr/bin/python3
""" Module that defines a class Square """


class Square:
    """ Class that defines a square """
    __size = None

    def area(self):
        """ Method that returns the area of the square """
        return self.__size * self.__size

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
