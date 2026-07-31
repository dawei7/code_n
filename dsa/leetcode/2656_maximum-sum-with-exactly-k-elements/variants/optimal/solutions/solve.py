def solve(nums: list[int], k: int) -> int:
    maximum = max(nums)
    return k * maximum + k * (k - 1) // 2
