def solve(nums: list[int], k: int) -> int:
    return (max(nums) - min(nums)) * k
