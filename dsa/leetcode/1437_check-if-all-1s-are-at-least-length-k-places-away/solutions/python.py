def solve(nums, k):
    previous = None
    for index, value in enumerate(nums):
        if value == 1:
            if previous is not None and index - previous <= k:
                return False
            previous = index
    return True
