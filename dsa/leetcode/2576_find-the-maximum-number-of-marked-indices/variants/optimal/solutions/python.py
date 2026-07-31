def solve(nums: list[int]) -> int:
    nums.sort()
    small = 0
    large = len(nums) // 2

    while small < len(nums) // 2 and large < len(nums):
        if 2 * nums[small] <= nums[large]:
            small += 1
        large += 1

    return 2 * small
