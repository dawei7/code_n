"""Prefix-sum weighted selection for LeetCode 528."""

from bisect import bisect_right
from itertools import accumulate


def solve(weights: list[int], random_values: list[float]) -> list[int]:
    prefix_sums = list(accumulate(weights))
    total = prefix_sums[-1]
    return [bisect_right(prefix_sums, value * total) for value in random_values]
