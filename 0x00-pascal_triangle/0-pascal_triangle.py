#!/usr/bin/python3
"""
    Pascal triangle representation
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing the Pascal's triangle
        of n

        Args:
            n: number the triangle should stop
    """
    final_list = [[1]]
    inner_list = list()
    i = 0

    if n <= 0:
        return []
    if n == 1:
        return final_list

    while i < n - 1:
        final_inner = [1]

        for ind in range(len(inner_list) - 1):
            final_inner.append(inner_list[ind] + inner_list[ind + 1])

        final_inner.append(1)
        final_list.append(final_inner)
        inner_list = final_inner
        i = i + 1

    return final_list
