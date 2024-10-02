#!/usr/bin/python3
""" Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """ n is the length of the row
    """
    triangle = []

    if n <= 0:
        return []

    for count in range(n):
        row = [1] * (count + 1)

        for column in range(1, count):
            row[column] = triangle[count - 1][column - 1] + \
            triangle[count - 1][column]

        triangle.append(row)

    return triangle
