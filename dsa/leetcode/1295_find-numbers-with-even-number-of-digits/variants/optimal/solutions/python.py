def solve(nums):
    count = 0
    for value in nums:
        if 10 <= value <= 99 or 1000 <= value <= 9999 or value == 100000:
            count += 1
    return count
