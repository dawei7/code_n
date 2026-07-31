def solve(nums: list[int]) -> int:
    result = 0
    for value in nums:
        if value % 2 == 0:
            result |= value
    return result
