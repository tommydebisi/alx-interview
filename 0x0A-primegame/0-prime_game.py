#!/usr/bin/python3
"""
    Prime_game mod
"""


def isPrime(num):
    """
        returns true if it's a prime number or false
        if not
    """
    half_num = num // 2
    if half_num == 1:
        return True
    for i in range(2, half_num + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
        Takes in number of rounds `x` and a list of numbers
        to formulate set from to given the winner of all rounds which
        will be either Maria or Ben

        Args:
            x: number of rounds
            nums: array of numbers
    """
    current, m_win, b_win = '', 0, 0
    if not nums:
        return None

    # cache prime numbers needed to complete prime game
    prime_list = [num for num in range(2, max(nums)) if isPrime(num)]

    for round in range(x):
        # maria starts first
        current = 'Maria'

        populate_num = nums[round]
        if not populate_num:
            continue

        if populate_num == 1:
            b_win += 1
            continue

        while populate_num not in prime_list:
            populate_num -= 1

        populated_list = prime_list[:prime_list.index(populate_num) + 1]

        for n in populated_list:
            # next person's turn to pick
            current = 'Maria' if current == 'Ben' else 'Ben'

        if current == 'Ben':
            m_win += 1
        else:
            b_win += 1

    if b_win > m_win:
        return 'Ben'
    if b_win < m_win:
        return 'Maria'
    return None
