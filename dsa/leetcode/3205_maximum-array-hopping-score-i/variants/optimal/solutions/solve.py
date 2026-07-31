def solve(nums: list[int]) -> int:
    suffix_maximum = 0
    score = 0
    for index in range(len(nums) - 1, 0, -1):
        suffix_maximum = max(suffix_maximum, nums[index])
        score += suffix_maximum
    return score
