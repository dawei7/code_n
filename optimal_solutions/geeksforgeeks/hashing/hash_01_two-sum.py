"""Optimal solution for hash_01: Two Sum.

Single pass: walk the array, for each value check whether
target - value has been seen. If yes, return the two indices.
Otherwise, store the current value's index in the map. O(n).
"""


def solve(arr, target, n):
    seen = {}
    for i in range(n):
        complement = target - arr[i]
        if complement in seen:
            return sorted([seen[complement], i])
        seen[arr[i]] = i
    return [-1, -1]
