#!/usr/bin/python3
"""
    0-minoperations mod
"""
from sympy import isprime


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

    if isprime(n):
        return n

    if n % 2 == 0:
        val = even_operation(n)
        if not isprime(val) and val % 2 != 0:
            val = odd_divisor(val)
    else:
        val = odd_divisor(n)

    return val if val % 2 == 0 else val + (n // val)


def even_operation(num):
    """
        calculates the fewest number of operations for even numbers

        Args:
            num: number to check for

        Returns:
            even number which is the fewest or odd number which is not sure
    """
    num //= 2

    if not isprime(num) and num % 2 == 0:
        num = even_operation(num)

    return num if num % 2 != 0 else num + 2


def odd_divisor(num):
    """
        calculates the least possible divisor of num
    """
    for i in range(3, num // 2):
        if num % i == 0:
            return i
