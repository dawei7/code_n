# Time:  O(n)
# Space: O(1)

import fractions


class Solution:
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return fractions.gcd(min(nums), max(nums))
