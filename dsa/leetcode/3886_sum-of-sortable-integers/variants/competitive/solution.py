# Time:  O(nlog(logn))
# Space: O(n)

# prefix sum, number theory
class Solution:
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(k):
            return len(nums)%k == 0 and all(prefix[i] <= suffix[i] and (prefix2[i+k-1]-prefix2[i])+(1 if nums[i+k-1] > nums[i] else 0) <= 1 for i in range(0, len(nums), k))

        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = max(prefix[i], nums[i])
        suffix = [float("inf")]*(len(nums)+1)
        for i in reversed(range(len(nums))):
            suffix[i] = min(suffix[i+1], nums[i])
        prefix2 = [0]*(len(nums))
        for i in range(len(nums)-1):
            prefix2[i+1] = prefix2[i]+(1 if nums[i] > nums[i+1] else 0)
        return sum(k for k in range(1, len(nums)+1) if check(k))
