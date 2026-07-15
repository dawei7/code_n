"""Optimal app-local solution for LeetCode 1427."""


def solve(s: str, shift: list[list[int]]) -> str:
    net_right = sum(amount if direction == 1 else -amount for direction, amount in shift)
    net_right %= len(s)
    if net_right == 0:
        return s
    return s[-net_right:] + s[:-net_right]
