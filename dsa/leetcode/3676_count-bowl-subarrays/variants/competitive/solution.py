# Time:  O(n)
# Space: O(n)

# mono stack
class Solution:
    def bowlSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        stk = []
        for i in range(len(nums)):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
                if stk:
                    result += 1
            stk.append(i)
        return result
