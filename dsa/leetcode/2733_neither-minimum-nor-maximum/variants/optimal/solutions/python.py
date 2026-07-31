def solve(nums):
    if len(nums) < 3:
        return -1

    a, b, c = nums[:3]
    return a + b + c - min(a, b, c) - max(a, b, c)
