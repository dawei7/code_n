"""Optimal solution for LeetCode 1063: Number of Valid Subarrays."""


def solve(nums: list[int]) -> int:
    unresolved: list[int] = []
    answer = 0

    for current, value in enumerate(nums):
        while unresolved and nums[unresolved[-1]] > value:
            start = unresolved.pop()
            answer += current - start
        unresolved.append(current)

    length = len(nums)
    while unresolved:
        answer += length - unresolved.pop()
    return answer
