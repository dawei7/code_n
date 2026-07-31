def solve(nums: list[int]) -> list[int]:
    length = len(nums)
    return [nums[(index + offset) % length] for index, offset in enumerate(nums)]
