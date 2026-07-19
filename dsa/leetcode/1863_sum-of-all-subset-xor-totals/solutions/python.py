def solve(nums: list[int]) -> int:
    combined_bits = 0
    for value in nums:
        combined_bits |= value
    return combined_bits << (len(nums) - 1)
