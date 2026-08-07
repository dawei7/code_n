# Time:  O(n + 26)
# Space: O(26)

# freq table
class Solution:
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        total = sum(cost)
        cnt = [0]*26
        for i in range(len(s)):
            cnt[ord(s[i])-ord('a')] += cost[i]
        return total-max(cnt)
