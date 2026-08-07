from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder_counts = Counter(number % value for number in nums)
        mex = 0

        while remainder_counts[mex % value]:
            remainder_counts[mex % value] -= 1
            mex += 1

        return mex
