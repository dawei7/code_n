"""Optimal solution for LeetCode 1010: Pairs of Songs With Total Durations Divisible by 60."""


def solve(time: list[int]) -> int:
    counts = [0] * 60
    pairs = 0
    for duration in time:
        remainder = duration % 60
        pairs += counts[-remainder % 60]
        counts[remainder] += 1
    return pairs
