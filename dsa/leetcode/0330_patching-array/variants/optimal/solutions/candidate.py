def solve(nums: list[int], n: int) -> int:
    missing = 1
    i = 0
    patches = 0
    while missing <= n:
        if i < len(nums) and nums[i] <= missing:
            missing += nums[i]
            i += 1
        else:
            missing += missing
            patches += 1
    return patches
