# Time:  O(n)
# Space: O(1)

import collections


class Solution:
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(set(collections.Counter(s).itervalues())) == 1
