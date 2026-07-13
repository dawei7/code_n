"""Whole-string uncommon-subsequence observation for LeetCode 521."""


def solve(a: str, b: str) -> int:
    return -1 if a == b else max(len(a), len(b))
