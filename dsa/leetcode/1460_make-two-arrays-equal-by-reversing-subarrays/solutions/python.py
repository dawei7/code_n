from collections import Counter


def solve(target, arr):
    return Counter(target) == Counter(arr)
