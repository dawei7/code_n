from __future__ import annotations


def solve(s: str) -> int:
    zeros = 0
    seconds = 0

    for char in s:
        if char == "0":
            zeros += 1
        elif zeros:
            seconds = max(zeros, seconds + 1)

    return seconds
