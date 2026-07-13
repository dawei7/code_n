"""Longest cyclic run per ending character for LeetCode 467."""


def solve(p: str) -> int:
    longest = [0] * 26
    run = 0
    for index, character in enumerate(p):
        if index > 0 and (ord(character) - ord(p[index - 1])) % 26 == 1:
            run += 1
        else:
            run = 1
        ending = ord(character) - ord("a")
        if run > longest[ending]:
            longest[ending] = run
    return sum(longest)
