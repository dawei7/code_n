from typing import List


def solve(nums: List[int], k: int) -> int:
    nums.sort()
    middle = len(nums) // 2
    operations = 0

    for index in range(middle + 1):
        if nums[index] > k:
            operations += nums[index] - k

    for index in range(middle, len(nums)):
        if nums[index] < k:
            operations += k - nums[index]

    return operations
