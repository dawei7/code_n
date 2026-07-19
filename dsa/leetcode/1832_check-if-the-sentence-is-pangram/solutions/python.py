"""App-local reference solution for LeetCode 1832."""


def solve(sentence: str) -> bool:
    return len(set(sentence)) == 26
