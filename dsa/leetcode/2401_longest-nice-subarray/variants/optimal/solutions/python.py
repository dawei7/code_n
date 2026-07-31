def solve(nums: list[int]) -> int:
    used_bits = 0
    left = 0
    best = 0

    for right, value in enumerate(nums):
        while used_bits & value:
            used_bits ^= nums[left]
            left += 1
        used_bits |= value
        best = max(best, right - left + 1)

    return best
