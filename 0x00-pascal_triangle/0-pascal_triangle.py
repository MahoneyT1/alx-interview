#!/usr/bin/python3

""" Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(number):
    """ n is the length of the row
    """
    if number <= 0:
        return []

    tri = []

    for i in range(number):
        # the first leading cell must start with 1
        row = [1] * (i + 1)

        for k in range(1, i):
            # the next row number is based on this
            # adding the two number above
            row[k] = tri[i - 1][k - 1] + tri[i - 1][k]

        tri.append(row)

    return tri


