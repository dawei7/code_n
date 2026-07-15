"""Optimal app-local solution for LeetCode 1408."""


def solve(words: list[str]) -> list[str]:
    matches: list[str] = []
    for index, word in enumerate(words):
        if any(
            index != other_index and word in other
            for other_index, other in enumerate(words)
        ):
            matches.append(word)
    return matches
