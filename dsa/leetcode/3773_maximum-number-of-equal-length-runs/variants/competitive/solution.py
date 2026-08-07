# Time:  O(n)
# Space: O(sqrt(n))

import collections


# freq table
class Solution:
    def maxSameLengthRuns(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        l = 0
        for i in range(len(s)):
            l += 1
            if i+1 == len(s) or s[i+1] != s[i]:
                cnt[l] += 1
                l = 0
        return max(cnt.values())


# Time:  O(n)
# Space: O(n)
# freq table
class Solution2(object):
    def maxSameLengthRuns(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = [0]*(len(s)+1)
        l = 0
        for i in range(len(s)):
            l += 1
            if i+1 == len(s) or s[i+1] != s[i]:
                cnt[l] += 1
                l = 0
        return max(cnt)
