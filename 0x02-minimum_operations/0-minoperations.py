#!/usr/bin/python3
"""
This module contains the minOperations function that calculates
the minimum number of operations needed to achieve exactly n H characters.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result in
    exactly n 'H' characters in the file.

    Args:
        n (int): The number of H characters desired.

    Returns:
        int: The fewest number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
