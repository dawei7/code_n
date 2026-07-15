"""Optimal app-local solution for LeetCode 982."""

from collections import Counter


def solve(nums):
    value_counts = Counter(nums)
    pair_counts = Counter(
        first & second
        for first in nums
        for second in nums
    )

    answer = 0
    for value, occurrences in value_counts.items():
        compatible_pairs = sum(
            count
            for mask, count in pair_counts.items()
            if mask & value == 0
        )
        answer += occurrences * compatible_pairs
    return answer
