def solve(nums: list[int]) -> int:
    maximum = 0
    score = 0

    for value in nums[:-1]:
        maximum = max(maximum, value)
        score += maximum

    return score
