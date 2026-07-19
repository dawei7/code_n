"""Optimal app-local solution for LeetCode 843."""

from collections import Counter


def solve(words, master):
    def matches(first, second):
        return sum(left == right for left, right in zip(first, second))

    candidates = list(words)
    while candidates:
        guess = min(
            candidates,
            key=lambda word: max(Counter(matches(word, candidate) for candidate in candidates).values()),
        )
        score = master.guess(guess)
        if score == 6:
            return master
        candidates = [candidate for candidate in candidates if matches(guess, candidate) == score]

    return master
