#!/usr/bin/python3
"""
    making-change mod
"""


def makeChange(coins, total):
    """
        get the smallest number of change to make from each coin
    """
    if total <= 0:
        return 0

    coin_list = sorted(coins)[::-1]
    length = len(coin_list)

    for coin in coin_list:
        c_index = coin_list.index(coin)
        result = getSumChange(coin_list[c_index:], total, 0, 0)

        if result[0] == total:
            return result[1]
    return -1


def getSumChange(rev_coins, total, coin_sum, coin_count):
    """
        returns a tuple of the coin_sum and the coin count
    """
    if coin_sum >= total or len(rev_coins) == 1:
        return (coin_sum, coin_count)

    c_sum, c_count = coin_sum, coin_count
    c_sum += rev_coins[0]
    c_count += 1

    if c_sum > total:
        c_sum -= rev_coins[0]
        c_count -= 1
        return getSumChange(rev_coins[1:], total, c_sum, c_count)
    else:
        return getSumChange(rev_coins, total, c_sum, c_count)
