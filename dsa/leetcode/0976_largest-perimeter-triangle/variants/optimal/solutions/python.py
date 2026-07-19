"""Optimal app-local solution for LeetCode 976."""


def solve(nums):
    lengths = sorted(nums, reverse=True)
    for i in range(len(lengths) - 2):
        if lengths[i + 1] + lengths[i + 2] > lengths[i]:
            return lengths[i] + lengths[i + 1] + lengths[i + 2]
    return 0
