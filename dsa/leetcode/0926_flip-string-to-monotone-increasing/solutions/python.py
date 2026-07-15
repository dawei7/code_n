"""Optimal app-local solution for LeetCode 926."""


def solve(s):
    ones_seen = 0
    flips = 0

    for character in s:
        if character == "1":
            ones_seen += 1
        else:
            flips = min(flips + 1, ones_seen)

    return flips

