def solve(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result
