def solve(nums: list[int]) -> int:
    jumps = 0
    current_end = 0
    farthest = 0
    for index in range(len(nums) - 1):
        farthest = max(farthest, index + nums[index])
        if index == current_end:
            jumps += 1
            current_end = farthest
    return jumps
