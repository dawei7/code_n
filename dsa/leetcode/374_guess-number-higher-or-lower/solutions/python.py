"""Optimal app-local solution for LeetCode 374: Guess Number Higher or Lower."""


def solve(n: int, pick: int) -> int:
    left = 1
    right = n

    while left <= right:
        middle = left + (right - left) // 2
        if middle == pick:
            return middle
        if middle > pick:
            right = middle - 1
        else:
            left = middle + 1

    raise ValueError("pick must lie between 1 and n")

