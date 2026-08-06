def solve(nums: list[int]) -> None:
    for i in range(1, len(nums)):
        should_swap = (i % 2 == 1 and nums[i - 1] > nums[i]) or (i % 2 == 0 and nums[i - 1] < nums[i])
        if should_swap:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
