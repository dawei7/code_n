def solve(nums: list[int]) -> int:
    count = 0
    for index in range(len(nums) - 2):
        if 2 * (nums[index] + nums[index + 2]) == nums[index + 1]:
            count += 1
    return count
