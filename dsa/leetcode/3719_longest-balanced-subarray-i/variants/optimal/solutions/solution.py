from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        longest = 0

        for left in range(len(nums)):
            distinct_even = set()
            distinct_odd = set()

            for right in range(left, len(nums)):
                value = nums[right]
                if value % 2 == 0:
                    distinct_even.add(value)
                else:
                    distinct_odd.add(value)

                if len(distinct_even) == len(distinct_odd):
                    longest = max(longest, right - left + 1)

        return longest
