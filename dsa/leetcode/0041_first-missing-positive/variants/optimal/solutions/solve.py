def solve(nums: list[int]) -> int:
    size = len(nums)
    for index in range(size):
        while 1 <= nums[index] <= size and nums[nums[index] - 1] != nums[index]:
            destination = nums[index] - 1
            nums[index], nums[destination] = nums[destination], nums[index]
    for index, value in enumerate(nums):
        if value != index + 1:
            return index + 1
    return size + 1
