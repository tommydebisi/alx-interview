#!/usr/bin/python3
"""
    Prime_game mod
"""


def isWinner(x, nums):
    """
        Takes in number of rounds `x` and a list of numbers
        to formulate set from to given the winner of all rounds which
        will be either Maria or Ben

        Args:
            x: number of rounds
            nums: array of numbers
    """
    if x != len(nums) or not nums:
        return None
    current, m_win, b_win = '', 0, 0
    for round in range(x):
        # maria starts first
        current = 'Maria'

        populate_num = nums[round]
        populated_list = [num for num in range(1, populate_num + 1)]

        while len(populated_list) > 1:
            prime = populated_list[1]

            # get multiples of prime
            p_multi = [i * prime for i in range(len(populated_list))
                       if (i * prime) in populated_list]

            # map through and remove all multiples in populated list
            for num in p_multi:
                populated_list.remove(num)

            # nect person's turn to pick
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
