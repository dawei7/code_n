"""Optimal solution for LeetCode 1078: Occurrences After Bigram."""


def solve(text: str, first: str, second: str) -> list[str]:
    words = text.split()
    return [
        words[index + 2]
        for index in range(len(words) - 2)
        if words[index] == first and words[index + 1] == second
    ]
