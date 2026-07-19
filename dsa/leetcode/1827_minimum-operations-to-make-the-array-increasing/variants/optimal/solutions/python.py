"""App-local reference solution for LeetCode 1827."""


def solve(nums: list[int]) -> int:
    operations = 0
    previous = nums[0]
    for value in nums[1:]:
        adjusted = max(value, previous + 1)
        operations += adjusted - value
        previous = adjusted
    return operations
