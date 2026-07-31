def solve(nums: list[int], k: int) -> int:
    total = 0
    n = len(nums)

    for index, value in enumerate(nums):
        left_is_smaller = index < k or value > nums[index - k]
        right_is_smaller = index + k >= n or value > nums[index + k]
        if left_is_smaller and right_is_smaller:
            total += value

    return total
