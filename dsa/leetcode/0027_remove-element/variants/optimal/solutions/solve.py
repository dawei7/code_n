def solve(nums: list[int], val: int) -> int:
    write = 0
    for value in nums:
        if value != val:
            nums[write] = value
            write += 1
    return write
