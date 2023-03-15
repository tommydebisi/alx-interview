#!/usr/bin/python3
"""
    making-change mod
"""


def makeChange(coins, total):
    """
        get the smallest number of change to make from each coin
    """
    change = 0
    index = 0
    # sort coins in descending order
    coins.sort(reverse=True)
    while total > 0:
        if index >= len(coins):
            return -1
        if coins[index] <= total:
            total -= coins[index]
            change += 1
        else:
            index += 1
    return change
