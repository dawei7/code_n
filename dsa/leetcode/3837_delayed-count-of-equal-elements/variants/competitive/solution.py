# Time:  O(n)
# Space: O(n)

import collections


# freq table
class Solution:
    def delayedCount(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0]*len(nums)
        cnt = collections.defaultdict(int)
        for i in reversed(range(len(nums)-k)):
            result[i] = cnt[nums[i]]
            cnt[nums[i+k]] += 1
        return result
