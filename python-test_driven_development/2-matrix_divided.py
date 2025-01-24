#!/usr/bin/python3
"""
Module to divide all elements of a matrix
the matrix must be a list of lists of integers or floats
the function divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix
    return: new matrix
    """
    the_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(the_msg)
    if not all(type(row) is list for row in matrix):
        raise TypeError(the_msg)
    if not all(type(i) in [int, float] for row in matrix for i in row):
        raise TypeError(the_msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    return new_matrix
