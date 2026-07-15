"""Optimal app-local solution for LeetCode 1324."""


def solve(s):
    words = s.split()
    height = max(map(len, words))
    rows = []
    for row in range(height):
        characters = [word[row] if row < len(word) else " " for word in words]
        rows.append("".join(characters).rstrip())
    return rows
