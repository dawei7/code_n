"""Frequency-map counting for LeetCode 532."""

from collections import Counter


def solve(nums: list[int], k: int) -> int:
    frequencies = Counter(nums)
    if k == 0:
        return sum(frequency >= 2 for frequency in frequencies.values())
    return sum(value + k in frequencies for value in frequencies)
