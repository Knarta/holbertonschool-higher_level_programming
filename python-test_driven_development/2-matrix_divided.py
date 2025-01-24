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
    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError(the_msg)
        for i in row:
            row_len = len(row)
            if isinstance(i, (int, float)) is False:
                raise TypeError(the_msg)
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))
    return new_matrix
