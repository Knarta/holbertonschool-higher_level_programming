#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialization of the rectangle class"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
