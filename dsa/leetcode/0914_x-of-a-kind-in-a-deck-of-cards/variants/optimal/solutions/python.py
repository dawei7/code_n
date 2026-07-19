"""Optimal app-local solution for LeetCode 914."""

from collections import Counter
from math import gcd


def solve(deck):
    group_size = 0
    for frequency in Counter(deck).values():
        group_size = gcd(group_size, frequency)
        if group_size == 1:
            return False
    return group_size > 1

