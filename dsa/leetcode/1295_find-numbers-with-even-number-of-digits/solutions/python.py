def solve(nums):
    return sum(len(str(abs(value))) % 2 == 0 for value in nums)
