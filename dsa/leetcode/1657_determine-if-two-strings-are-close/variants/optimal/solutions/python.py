from collections import Counter


def solve(word1: str, word2: str) -> bool:
    first = Counter(word1)
    second = Counter(word2)
    return first.keys() == second.keys() and sorted(first.values()) == sorted(second.values())
