from bisect import bisect_left


class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        points = sorted(
            (index - value, value)
            for index, value in enumerate(nums)
            if value <= index
        )

        tails = []
        for _, value in points:
            position = bisect_left(tails, value)
            if position == len(tails):
                tails.append(value)
            else:
                tails[position] = value
        return len(tails)
