# Time:  O(n)
# Space: O(n)

# hash table
class Solution:
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        return len(set(nums[i]for i in range(len(nums)) if nums[i] != target[i]))
