"""App-local reference solution for LeetCode 2828."""

from typing import List


def solve(words: List[str], s: str) -> bool:
    """Return whether the ordered first characters form s exactly."""
    if len(words) != len(s):
        return False

    return all(word[0] == character for word, character in zip(words, s))
