# Time:  O(n)
# Space: O(1)

# greedy
class Solution:
    def largestInteger(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: int
        """
        result = 0
        for _ in range(n):
            x = min(s, 9)
            result = result*10+x
            s -= x
        return result if not s else -1
