def solve(nums: list[int]) -> int:
    return len(nums) - 1 if sum(nums) % 2 == 0 else 0
