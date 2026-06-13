"""Optimal solution for randomized_03: Fisher-Yates Shuffle.

Given an array of n elements, return a uniformly
"""


def solve(arr, n):
    """Fisher-Yates shuffle. Returns a new list."""
    import random
    work = list(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        work[i], work[j] = work[j], work[i]
    return work
