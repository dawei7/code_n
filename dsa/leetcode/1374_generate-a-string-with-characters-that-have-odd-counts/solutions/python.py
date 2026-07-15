"""Reference solution for LeetCode 1374."""


def solve(n: int) -> str:
    if n % 2 == 1:
        return "a" * n
    return "a" * (n - 1) + "b"
