# Time:  O(n)
# Space: O(1)

# array
class Solution:
    def reverseSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        l = len(nums)//k
        for i in range(0, len(nums), l):
            reverse(i, i+l-1)
        return nums
