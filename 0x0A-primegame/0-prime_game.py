#!/usr/bin/python3
"""
Mod.: Prime numbers choosing GAME
"""


def primeNumbers(n):
    """Returning prime numbers list between 1 and n inclusive
       Args:
        n (int): upper-end of range. lower-end is always 1
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Determines Prime Game Winner
    Args:
        x (int): no. of game rounds
        nums (int): upper-end range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
