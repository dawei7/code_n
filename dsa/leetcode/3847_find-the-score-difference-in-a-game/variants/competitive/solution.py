# Time:  O(n)
# Space: O(1)

# simulation
class Solution:
    def scoreDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        sign = 1
        for i in range(len(nums)):
            if nums[i]%2:
                sign *= -1
            if i%6 == 5:
                sign *= -1
            result += sign*nums[i]
        return result
