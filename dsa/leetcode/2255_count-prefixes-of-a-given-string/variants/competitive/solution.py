# Time:  O(n * l)
# Space: O(1)

import itertools


# string
class Solution:
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        return sum(itertools.imap(s.startswith, words))
