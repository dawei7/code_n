from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for value in nums:
            index = bisect_left(tails, value)
            if index == len(tails):
                tails.append(value)
            else:
                tails[index] = value
        return len(tails)
