"""Optimal solution for hash_03: Longest Substring Without Repeating.

Sliding window: extend the right end, record the last index of
each character seen. If a repeat sits inside the window, jump
the left end past the previous occurrence. O(n).
"""


def solve(s, n):
    if n == 0:
        return 0
    last = {}
    best = 0
    left = 0
    for right in range(n):
        ch = s[right]
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        if right - left + 1 > best:
            best = right - left + 1
    return best
