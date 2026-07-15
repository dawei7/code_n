"""Optimal app-local solution for LeetCode 1310."""


def solve(arr, queries):
    prefix = [0]
    for value in arr:
        prefix.append(prefix[-1] ^ value)

    return [prefix[right + 1] ^ prefix[left] for left, right in queries]
