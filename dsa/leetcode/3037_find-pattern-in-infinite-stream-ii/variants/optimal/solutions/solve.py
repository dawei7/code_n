"""Optimal app-local solution for LeetCode 3037."""


def solve(stream, pattern):
    prefix = [0] * len(pattern)
    matched = 0

    for index in range(1, len(pattern)):
        while matched and pattern[index] != pattern[matched]:
            matched = prefix[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        prefix[index] = matched

    matched = 0
    index = 0
    while True:
        bit = stream.next()
        while matched and bit != pattern[matched]:
            matched = prefix[matched - 1]
        if bit == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            return index - len(pattern) + 1
        index += 1
