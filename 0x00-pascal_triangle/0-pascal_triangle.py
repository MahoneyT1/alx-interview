#!/usr/bin/python3

""" Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """ n is the length of the row
    """
    if n <= 0:
        return []

    tri = [[1]]

    for i in range(1, n):
        # start each row initializing 1 to row
        row = [1]

        for j in range(1, i):
            row.append(tri[i - 1][j - 1] + tri[i - 1][j])

        # end each row with 1
        row.append(1)
        tri.append(row)

    return tri
