#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90
degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must
be edited in-place. You can assume the
matrix will have 2 dimensions and will
not be empty.
"""


def rotate_2d_matrix(matrix):
    """rotates 2d matrix, and exchange their values
    according to their position.
    """

    # initialize an empty list of list
    n = len(matrix)

    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = matrix[i][j]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]
