def solve(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    total = 0

    while left < right:
        multiplier = 10
        while multiplier <= nums[right]:
            multiplier *= 10

        total += nums[left] * multiplier + nums[right]
        left += 1
        right -= 1

    if left == right:
        total += nums[left]

    return total
