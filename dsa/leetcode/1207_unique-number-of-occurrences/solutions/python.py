from collections import Counter


def solve(arr):
    frequencies = Counter(arr).values()
    return len(set(frequencies)) == len(list(frequencies))
