def solve(nums):
    total = 0
    result = []

    for value in nums:
        total += value
        result.append(total)

    return result
