# Time:  O(n * p)
# Space: O(1)

# string
class Solution:
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return sum(x.startswith(pref) for x in words)
