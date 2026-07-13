"""Optimal app-local solution for LeetCode 422."""


def solve(words: list[str]) -> bool:
    for row, word in enumerate(words):
        for column, character in enumerate(word):
            if column >= len(words) or row >= len(words[column]):
                return False
            if words[column][row] != character:
                return False
    return True
