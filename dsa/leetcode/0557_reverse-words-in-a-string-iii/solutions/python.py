"""Independent word reversal for LeetCode 557."""


def solve(s: str) -> str:
    return " ".join(word[::-1] for word in s.split(" "))

