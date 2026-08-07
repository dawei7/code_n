# Time:  O(n)
# Space: O(1)

# greedy
class Solution:
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(max(nums[i]-nums[i+1], 0) for i in range(len(nums)-1))
