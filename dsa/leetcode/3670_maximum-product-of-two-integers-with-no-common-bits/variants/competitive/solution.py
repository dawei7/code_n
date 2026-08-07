# Time:  O(n + rlogr), r = max(nums)
# Space: O(r)

# dp, bitmasks
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = max(nums).bit_length()
        dp = [0]*(1<<l)
        for x in nums:
            dp[x] = x
        for i in range(l):
            for j in range(0, 1<<l, 1<<(i+1)):
                for k in range(j, j+(1<<i)):
                    if dp[k] > dp[k+(1<<i)]:
                        dp[k+(1<<i)] = dp[k]
        result = 0
        for x in nums:
            if x*dp[((1<<l)-1)^x] > result:
                result = x*dp[((1<<l)-1)^x]
        return result


# Time:  O(n + rlogr), r = max(nums)
# Space: O(r)
# dp, bitmasks
class Solution2(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = max(nums).bit_length()
        dp = [0]*(1<<l)
        for x in nums:
            dp[x] = x
        for i in range(l):
            for mask in range(1<<l):
                if mask&(1<<i):
                    continue
                if dp[mask] > dp[mask|(1<<i)]:
                    dp[mask|(1<<i)] = dp[mask]
        result = 0
        for x in nums:
            if x*dp[((1<<l)-1)^x] > result:
                result = x*dp[((1<<l)-1)^x]
        return result
