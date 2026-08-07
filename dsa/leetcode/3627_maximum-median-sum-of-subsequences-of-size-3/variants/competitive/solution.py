# Time:  O(nlogn)
# Space: O(1)

# sort, greedy
class Solution:
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[i] for i in range(len(nums)//3, len(nums), 2))
