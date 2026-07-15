"""Optimal app-local solution for LeetCode 846."""

from collections import Counter


def solve(hand, group_size):
    if len(hand) % group_size != 0:
        return False

    counts = Counter(hand)
    for start in sorted(counts):
        copies = counts[start]
        if copies == 0:
            continue
        for value in range(start, start + group_size):
            if counts[value] < copies:
                return False
            counts[value] -= copies

    return True
