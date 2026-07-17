def solve(nums: list[int], k: int) -> list[int]:
    best_start = 0
    for start in range(1, len(nums) - k + 1):
        if nums[start] > nums[best_start]:
            best_start = start
    return nums[best_start : best_start + k]
