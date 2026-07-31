def solve(nums: list[int], k: int) -> list[int]:
    start = max(range(len(nums) - k + 1), key=nums.__getitem__)
    return nums[start : start + k]
