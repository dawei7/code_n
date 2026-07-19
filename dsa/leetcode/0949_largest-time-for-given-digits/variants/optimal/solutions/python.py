"""Optimal app-local solution for LeetCode 949."""

from itertools import permutations


def solve(arr):
    best = -1
    for first, second, third, fourth in permutations(arr):
        hour = first * 10 + second
        minute = third * 10 + fourth
        if hour < 24 and minute < 60:
            best = max(best, hour * 60 + minute)

    if best < 0:
        return ""
    return f"{best // 60:02d}:{best % 60:02d}"
