def solve(nums: list[int]) -> None:
    write = 0
    for read, value in enumerate(nums):
        if value != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
