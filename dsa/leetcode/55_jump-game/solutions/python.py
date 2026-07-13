def solve(nums: list[int]) -> bool:
    farthest = 0
    for index, jump in enumerate(nums):
        if index > farthest:
            return False
        farthest = max(farthest, index + jump)
        if farthest >= len(nums) - 1:
            return True
    return True
