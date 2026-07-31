"""Optimal app-local solution for LeetCode 425."""

from collections import defaultdict


def solve(words: list[str]) -> list[list[str]]:
    word_length = len(words[0])
    by_prefix: dict[str, list[str]] = defaultdict(list)
    for word in words:
        for length in range(word_length + 1):
            by_prefix[word[:length]].append(word)

    answer: list[list[str]] = []
    square: list[str] = []

    def search() -> None:
        row = len(square)
        if row == word_length:
            answer.append(square.copy())
            return

        prefix = "".join(square[previous][row] for previous in range(row))
        for candidate in by_prefix.get(prefix, []):
            square.append(candidate)
            search()
            square.pop()

    search()
    return answer
