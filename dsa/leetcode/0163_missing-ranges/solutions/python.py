def solve(nums: list[int], lower: int, upper: int) -> list[list[int]]:
    ranges: list[list[int]] = []
    next_missing = lower
    for value in nums:
        if next_missing < value:
            ranges.append([next_missing, value - 1])
        next_missing = value + 1
    if next_missing <= upper:
        ranges.append([next_missing, upper])
    return ranges
