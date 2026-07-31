def solve(nums: list[int]) -> int:
    total = sum(nums)
    if len(nums) % 2 == 1:
        return total - min(nums)

    minimum_pair = min(nums[index] + nums[index + 1] for index in range(len(nums) - 1))
    return total - minimum_pair
