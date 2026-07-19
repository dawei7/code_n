from collections import Counter


def solve(arr: list[int]) -> bool:
    frequencies = Counter(arr).values()
    return len(set(frequencies)) == len(frequencies)
