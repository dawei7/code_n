"""Optimal solution for LeetCode 1403: Minimum Subsequence in Non-Increasing Order."""


def solve(nums: list[int]) -> list[int]:
    nums.sort(reverse=True)
    total = sum(nums)
    chosen = 0
    result: list[int] = []
    for value in nums:
        result.append(value)
        chosen += value
        if chosen > total - chosen:
            return result
    return result
