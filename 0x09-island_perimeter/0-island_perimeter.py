#!/usr/bin/python3
"""
    Island perimeter module
"""


def island_perimeter(grid):
    """
        returns the permiter of island
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                peri_tuple = checkHorizontalVertical(grid, perimeter, row, col)

                if peri_tuple[1] == 4:
                    return peri_tuple[1]

                perimeter += peri_tuple[0]
    return perimeter


def checkHorizontalVertical(grid, current_peri, row, col):
    """
        checks the grid horizontally and vertically
    """
    perimeter = 0
    count = 0

    if grid[row][col - 1] == 0:
        perimeter += 1
        count += 1

    if grid[row][col + 1] == 0:
        perimeter += 1
        count += 1

    if grid[row - 1][col] == 0:
        perimeter += 1
        count += 1

    if grid[row + 1][col] == 0:
        perimeter += 1
        count += 1

    if count == 4:
        return (perimeter, count)
    return (perimeter, 0)
