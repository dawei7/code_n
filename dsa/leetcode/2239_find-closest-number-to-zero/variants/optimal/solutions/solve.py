def solve(nums: list[int]) -> int:
    closest = nums[0]
    for value in nums[1:]:
        if abs(value) < abs(closest) or (abs(value) == abs(closest) and value > closest):
            closest = value
    return closest
