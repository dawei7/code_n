def solve(nums: list[int], target: int, start: int) -> int:
    return min(abs(index - start) for index, value in enumerate(nums) if value == target)
