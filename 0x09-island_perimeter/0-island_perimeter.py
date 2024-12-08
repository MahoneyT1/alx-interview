#!/usr/bin/python3

""" Module with island_perimeter function that returns the perimeter
of an island described in grid.
grid will be list of integers.
0 represents water and 1 represents land.
Each cell is a square with side length 1. And are connected
horizontally/vertically.
Grid is completely surrounded by water, and there is exactly one island.
No lakes (water inside that isn't connected to the water around the island).

Problem Description:-
You're given a 2D grid map of a binary matrix where:
    0 represents water. 1 represents land.
    The goal is to calculate the perimeter of the island.
    The island is defined as a group of 1s (land) connected 4-directionally
        (horizontal or vertical).
    There may be multiple islands, but we need to find the perimeter
        of one single island (if there's more than one).

Approach:-
Iterate through each cell in the grid.
Count the perimeter for each land cell by checking its four neighboring cells:
    If a neighboring cell is water (or out of bounds), it contributes
        to the perimeter.
    If a neighboring cell is also land, it does not contribute
        to the perimeter for that edge.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid: List[List[int]] list of list of int - 2D grid map of 0s and 1s.

    Return:
        int: perimeter of the island.
    """

    if not grid:  # if not grid, nothing to compute for, return 0
        return 0

    # determine number of rows and columns in grid & init perimeter to 0
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    # use nested loop to iterate through each cell in grid
    for r in range(rows):
        for c in range(cols):
            # check for each cell if it contains land
            if grid[r][c] == 1:  # land cell
                # check all 4 directions (up, down, left, right) for water
                # if water is found, increment perimeter by 1
                if r == 0 or grid[r - 1][c] == 0:  # check cells above
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # check cells below
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # check cells to the left
                    perimeter += 1
                # check cells to the right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
