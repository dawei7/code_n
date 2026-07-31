def solve(nums: list[int], k: int) -> list[int]:
    write = 0

    for value in nums:
        if write < k or nums[write - k] != value:
            nums[write] = value
            write += 1

    del nums[write:]
    return nums
