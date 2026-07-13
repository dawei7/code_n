"""Prefix-sum query structure for LeetCode 303."""


class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    num_array = NumArray(nums)
    return [num_array.sumRange(left, right) for left, right in queries]
