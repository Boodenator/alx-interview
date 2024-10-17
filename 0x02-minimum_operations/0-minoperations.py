#!/usr/bin/python3

"""
    Way to determine the number of minmum operations with n characters
"""


def minOperations(n):
    """
        Function calculateing the least no of operations
        required to give result of exactly n H characters in file
        args: n: No. of characters displayed
        return:
               no of min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
