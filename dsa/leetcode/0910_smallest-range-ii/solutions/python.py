"""Optimal app-local solution for LeetCode 910."""


def solve(nums, k):
    values = sorted(nums)
    best = values[-1] - values[0]

    for index in range(len(values) - 1):
        high = max(values[index] + k, values[-1] - k)
        low = min(values[0] + k, values[index + 1] - k)
        best = min(best, high - low)

    return best
