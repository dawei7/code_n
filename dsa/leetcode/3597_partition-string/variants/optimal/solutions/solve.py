"""Optimal app-local solution for LeetCode 3597."""


def solve(s):
    root = {}
    segments = []
    start = 0

    while start < len(s):
        node = root
        end = start

        while end < len(s) and s[end] in node:
            node = node[s[end]]
            end += 1

        if end == len(s):
            break

        node[s[end]] = {}
        segments.append(s[start : end + 1])
        start = end + 1

    return segments
