def solve(nums: list[list[int]]) -> int:
    for row in nums:
        row.sort()
    return sum(max(column) for column in zip(*nums))
