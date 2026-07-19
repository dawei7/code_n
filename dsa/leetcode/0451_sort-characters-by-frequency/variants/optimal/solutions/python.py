"""Linear bucket-sort solution for LeetCode 451."""

from collections import Counter


def solve(s: str) -> str:
    frequencies = Counter(s)
    buckets: list[list[str]] = [[] for _ in range(len(s) + 1)]
    for character, frequency in frequencies.items():
        buckets[frequency].append(character)

    pieces: list[str] = []
    for frequency in range(len(s), 0, -1):
        for character in buckets[frequency]:
            pieces.append(character * frequency)
    return "".join(pieces)
