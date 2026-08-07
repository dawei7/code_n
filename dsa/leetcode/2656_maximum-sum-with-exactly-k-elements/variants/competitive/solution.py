# Time:  O(n)
# Space: O(1)

# math
class Solution:
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(nums)*k+k*(k-1)//2
