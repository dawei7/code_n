# Time:  O(n)
# Space: O(1)

import collections


class Solution:
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False 
        
        cnt1, cnt2 = collections.Counter(word1), collections.Counter(word2)   # Reuse of keys
        return set(cnt1.keys()) == set(cnt2.keys()) and \
               collections.Counter(cnt1.values()) == collections.Counter(cnt2.values())
