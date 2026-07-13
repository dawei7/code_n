"""At-most-one-zero sliding window for LeetCode 487."""


def solve(nums: list[int]) -> int:
    left = 0
    zero_count = 0
    best = 0

    for right, value in enumerate(nums):
        if value == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        best = max(best, right - left + 1)

    return best
