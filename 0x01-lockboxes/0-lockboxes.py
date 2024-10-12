#!/usr/bin/python3
"""Unlock list of lists using script"""


def canUnlockAll(boxes):
    """Function to intake a list of lists in order to
       unlock other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
