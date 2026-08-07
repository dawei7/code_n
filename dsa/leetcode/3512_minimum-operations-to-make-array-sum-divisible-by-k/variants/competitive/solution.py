# Time:  O(n)
# Space: O(1)

# math
class Solution:
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(nums)%k
