# Time:  O(nlogn)
# Space: O(n)

import collections


class Solution:
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
