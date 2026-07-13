"""Per-bit pair counting for LeetCode 477."""


def solve(nums: list[int]) -> int:
    total = 0
    width = max(nums, default=0).bit_length()
    for bit in range(width):
        ones = 0
        for value in nums:
            ones += (value >> bit) & 1
        total += ones * (len(nums) - ones)
    return total
