def solve(nums: list[int], k: int) -> int:
    return sum(value < k for value in nums)
