"""Optimal app-local solution for LeetCode 1143."""


def solve(text1: str, text2: str) -> int:
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    previous = [0] * (len(text2) + 1)
    for first in text1:
        current = [0] * (len(text2) + 1)
        for column, second in enumerate(text2, start=1):
            if first == second:
                current[column] = previous[column - 1] + 1
            else:
                current[column] = max(previous[column], current[column - 1])
        previous = current
    return previous[-1]
