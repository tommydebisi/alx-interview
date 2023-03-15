#!/usr/bin/python3
"""
    Island perimeter module
"""


def island_perimeter(grid):
    """
        returns the permiter of island
    """
    if type(grid) is not list:
        return 0
    if not all([type(row) is list for row in grid]):
        return 0
    if not all([len(row) == len(grid[0]) for row in grid]):
        return 0

    perimeter = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            m, n = len(grid) - 1, len(row) - 1
            neighbors = (
                i > 0 and grid[i-1][j] == 1,    # top
                i < m and grid[i+1][j] == 1,    # bottom
                j > 0 and grid[i][j-1] == 1,    # left
                j < n and grid[i][j+1] == 1,    # right
            )
            # add the contribution of this cell to the perimeter
            perimeter += 4 - sum(neighbors)
    return perimeter
