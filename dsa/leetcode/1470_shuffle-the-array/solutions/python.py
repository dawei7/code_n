def solve(nums, n):
    n = max(0, min(int(n), len(nums) // 2))
    result = []
    for index in range(n):
        result.append(nums[index])
        result.append(nums[index + n])
    result.extend(nums[2 * n:])
    return result
