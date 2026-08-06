def solve(nums: list[int]) -> int:
    size = len(nums)
    for i in range(size):
        while 1 <= nums[i] <= size and nums[nums[i] - 1] != nums[i]:
            destination = nums[i] - 1
            nums[i], nums[destination] = nums[destination], nums[i]
    for i, value in enumerate(nums):
        if value != i + 1:
            return i + 1
    return size + 1
