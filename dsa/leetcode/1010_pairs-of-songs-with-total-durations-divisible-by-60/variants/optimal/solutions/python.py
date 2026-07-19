"""Optimal app-local solution for LeetCode 1010."""


def solve(time):
    counts = [0] * 60
    pairs = 0

    for duration in time:
        remainder = duration % 60
        complement = (-remainder) % 60
        pairs += counts[complement]
        counts[remainder] += 1

    return pairs
