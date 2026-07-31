def solve(nums: list[int]) -> bool:
    n = len(nums)
    index = 1

    while index < n and nums[index] > nums[index - 1]:
        index += 1
    if index == 1 or index == n:
        return False

    decreasing_start = index
    while index < n and nums[index] < nums[index - 1]:
        index += 1
    if index == decreasing_start or index == n:
        return False

    increasing_start = index
    while index < n and nums[index] > nums[index - 1]:
        index += 1

    return index == n and index > increasing_start
