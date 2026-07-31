def solve(nums: list[int], original: int) -> int:
    values = set(nums)
    while original in values:
        original *= 2
    return original
