def solve(nums: list[int]) -> int:
    best = current = nums[0]

    for previous, value in zip(nums, nums[1:]):
        if value > previous:
            current += value
        else:
            current = value
        best = max(best, current)

    return best
