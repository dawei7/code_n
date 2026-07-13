def solve(nums: list[int]) -> None:
    for index in range(1, len(nums)):
        should_swap = (
            index % 2 == 1 and nums[index - 1] > nums[index]
        ) or (
            index % 2 == 0 and nums[index - 1] < nums[index]
        )
        if should_swap:
            nums[index - 1], nums[index] = nums[index], nums[index - 1]
