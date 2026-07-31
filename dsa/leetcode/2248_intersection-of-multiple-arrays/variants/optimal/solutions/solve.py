def solve(nums: list[list[int]]) -> list[int]:
    common = set(nums[0])
    for values in nums[1:]:
        common.intersection_update(values)
    return sorted(common)
