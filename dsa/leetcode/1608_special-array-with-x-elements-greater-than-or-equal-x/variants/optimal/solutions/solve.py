def solve(nums):
    nums.sort()
    length = len(nums)
    for index, value in enumerate(nums):
        candidate = length - index
        if value >= candidate and (index == 0 or nums[index - 1] < candidate):
            return candidate
    return -1
