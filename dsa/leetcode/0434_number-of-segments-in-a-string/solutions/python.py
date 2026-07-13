"""Optimal app-local solution for LeetCode 434."""


def solve(s: str) -> int:
    return sum(
        character != " " and (index == 0 or s[index - 1] == " ")
        for index, character in enumerate(s)
    )
