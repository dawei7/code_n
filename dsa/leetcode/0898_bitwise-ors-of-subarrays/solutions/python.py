"""Optimal app-local solution for LeetCode 898."""


def solve(arr):
    ending = set()
    results = set()

    for value in arr:
        ending = {value} | {previous | value for previous in ending}
        results.update(ending)

    return len(results)
