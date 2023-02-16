#!/usr/bin/python3
"""
    rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
        rotates a 2d matrix

        Args:
            matrix: 2d matrix provided
    """
    outer_list = []
    len_outer = len(matrix)

    for col in range(len_outer):
        inner_list = []
        for row in range(len(matrix[col])):
            inner_list.append(matrix[row][col])
        inner_list.reverse()
        outer_list.append(inner_list)

    # override current items with rotated matrix
    for item in range(len_outer):
        matrix[item] = outer_list[item]
