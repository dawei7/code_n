"""Optimal app-local solution for LeetCode 1170."""


def _frequency(value: str) -> int:
    smallest = "{"
    count = 0
    for character in value:
        if character < smallest:
            smallest = character
            count = 1
        elif character == smallest:
            count += 1
    return count


def solve(queries: list[str], words: list[str]) -> list[int]:
    counts = [0] * 11
    for word in words:
        counts[_frequency(word)] += 1

    greater = [0] * 11
    for frequency in range(9, 0, -1):
        greater[frequency] = greater[frequency + 1] + counts[frequency + 1]
    return [greater[_frequency(query)] for query in queries]
