def solve(nums: list[int]) -> list[int]:
    nums.sort()
    for index in range(0, len(nums) - 1, 2):
        nums[index], nums[index + 1] = nums[index + 1], nums[index]
    return nums
