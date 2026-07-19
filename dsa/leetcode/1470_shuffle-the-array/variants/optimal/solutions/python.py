def solve(nums, n):
    shuffled = []
    for index in range(n):
        shuffled.append(nums[index])
        shuffled.append(nums[index + n])
    return shuffled
