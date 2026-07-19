"""App-local reference solution for LeetCode 1822."""


def solve(nums: list[int]) -> int:
    sign = 1
    for value in nums:
        if value == 0:
            return 0
        if value < 0:
            sign = -sign
    return sign
