from bisect import bisect_left, bisect_right


def solve(nums: list[int]) -> int:
    negative = bisect_left(nums, 0)
    positive = len(nums) - bisect_right(nums, 0)
    return max(negative, positive)
