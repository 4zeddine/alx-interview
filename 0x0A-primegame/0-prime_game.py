#!/usr/bin/python3
"""Module for solving prime game"""


def isWinner(x, nums):
    """Return: name of the player that won the most rounds."""
    if x < 1 or not nums:
        return None
    winner_marias, winner_bens = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        winner_bens += primes_count % 2 == 0
        winner_marias += primes_count % 2 == 1
    if winner_marias == winner_bens:
        return None
    return 'Maria' if winner_marias > winner_bens else 'Ben'
