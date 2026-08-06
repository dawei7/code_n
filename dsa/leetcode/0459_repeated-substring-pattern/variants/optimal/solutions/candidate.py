"""Inert naming candidate for LeetCode 459."""


def solve(s: str) -> bool:
    prefix = [0] * len(s)
    border = 0
    for i in range(1, len(s)):
        while border and s[i] != s[border]:
            border = prefix[border - 1]
        if s[i] == s[border]:
            border += 1
        prefix[i] = border

    period = len(s) - prefix[-1]
    return prefix[-1] > 0 and len(s) % period == 0
