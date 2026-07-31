from typing import List


def solve(nums: List[int]) -> int:
    candidate = nums[0]
    balance = 0

    for value in nums:
        if balance == 0:
            candidate = value
        balance += 1 if value == candidate else -1

    total = nums.count(candidate)
    left = 0
    n = len(nums)

    for i in range(n - 1):
        if nums[i] == candidate:
            left += 1

        if left * 2 > i + 1 and (total - left) * 2 > n - i - 1:
            return i

    return -1
