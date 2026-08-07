# Time:  O(n)
# Space: O(1)

class Solution:
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "01" not in s
