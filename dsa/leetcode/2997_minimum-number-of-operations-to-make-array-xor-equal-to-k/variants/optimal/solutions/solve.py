def solve(nums, k):
    difference = k
    for value in nums:
        difference ^= value
    return difference.bit_count()
