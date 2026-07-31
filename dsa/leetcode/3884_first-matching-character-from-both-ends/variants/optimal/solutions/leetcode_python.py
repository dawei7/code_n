class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        for index in range(len(s)):
            if s[index] == s[len(s) - index - 1]:
                return index

        return -1
