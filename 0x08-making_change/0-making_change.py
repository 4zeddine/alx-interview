#!/usr/bin/python3
"""Module for making change."""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    rest = total
    counter = 0
    coins_id = 0
    coins_sorted = sorted(coins, reverse=True)
    n = len(coins)
    while rest > 0:
        if coins_id >= n:
            return -1
        if rest - coins_sorted[coins_id] >= 0:
            rest -= coins_sorted[coins_id]
            counter += 1
        else:
            coins_id += 1
    return counter
