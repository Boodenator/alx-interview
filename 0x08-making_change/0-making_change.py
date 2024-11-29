#!/usr/bin/python3
"""Function determining fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """The function will take a list of coins and use
       it to calculate the required totla change
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
