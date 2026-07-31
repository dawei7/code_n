def solve(nums: list[int], target: int) -> list[int]:
    smaller = sum(value < target for value in nums)
    equal = sum(value == target for value in nums)
    return list(range(smaller, smaller + equal))
