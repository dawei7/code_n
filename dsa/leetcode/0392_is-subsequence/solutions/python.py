"""Optimal app-local solution for LeetCode 392: Is Subsequence."""


def solve(s: str, t: str) -> bool:
    matched = 0

    for character in t:
        if matched < len(s) and character == s[matched]:
            matched += 1

    return matched == len(s)
