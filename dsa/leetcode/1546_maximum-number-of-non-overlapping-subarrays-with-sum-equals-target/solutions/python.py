def solve(nums, target):
    seen = {0}
    prefix = 0
    count = 0
    for num in nums:
        prefix += num
        if prefix - target in seen:
            count += 1
            seen = {0}
            prefix = 0
        else:
            seen.add(prefix)
    return count
