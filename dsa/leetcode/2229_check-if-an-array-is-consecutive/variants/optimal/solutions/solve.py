def solve(nums: list[int]) -> bool:
    distinct = set(nums)
    return len(distinct) == len(nums) and max(nums) - min(nums) == len(nums) - 1
