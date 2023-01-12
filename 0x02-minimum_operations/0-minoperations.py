#!/usr/bin/python3
"""
    0-minoperations mod
"""


def minOperations(n):
    """
        calculates the fewest number of operations needed to result in
        exactly n H characters in the file.

        Args:
            n (int): number of H characters

        Returns:
            int: fewest number of operations needed to result in exactly n H
    """
    if n <= 1 or not isinstance(n, int):
        return 0

    if isPrime(n):
        return n

    return even_odd_ops(n)


def even_odd_ops(num):
    """
        calculates the fewest number of operations for even
        and odd numbers

        Args:
            num: number to check for

        Returns:
            the fewest number of operations for a number
    """
    if isPrime(num):  # prime num can't be divided, return num
        return num
    else:
        if num % 2 != 0:  # check if odd number is passed in
            return odd_operation(num)

    return even_odd_ops(num // 2) + 2  # num is even, add 2


def odd_operation(odd_num):
    """
        calculates the fewest number of operations for an odd number
        passed in
    """
    prev = 0
    ops = 0

    for i in range(3, odd_num // 2):
        if odd_num % i == 0:  # check for multiples of odd number
            if prev == 0:
                ops = i
                prev = i
            elif i % prev == 0:  # check if current is divisible by prev
                ops += (i // prev)  # update operation
                prev = i

    return ops + (odd_num // prev)


def isPrime(num):
    """
        checks if a number is prime
    """
    if num <= 1:
        return False

    for i in range(2, num // 2):
        if num % i == 0:
            return False

    return True
