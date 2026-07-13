def solve(nums):
    left = 0
    zeros = 0
    best = 0
    for right, value in enumerate(nums):
        zeros += value == 0
        while zeros > 1:
            zeros -= nums[left] == 0
            left += 1
        best = max(best, right - left)
    return best
