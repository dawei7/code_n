def solve(nums: list[int]) -> int:
    for length in range(len(nums) - 1, 0, -1):
        for index in range(length):
            nums[index] = (nums[index] + nums[index + 1]) % 10
    return nums[0]
