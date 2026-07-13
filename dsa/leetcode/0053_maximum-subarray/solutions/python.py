def solve(nums: list[int]) -> int:
    ending_here = nums[0]
    best = nums[0]
    for value in nums[1:]:
        ending_here = max(value, ending_here + value)
        best = max(best, ending_here)
    return best
