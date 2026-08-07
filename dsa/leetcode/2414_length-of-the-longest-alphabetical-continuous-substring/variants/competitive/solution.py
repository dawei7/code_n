class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest = 1
        current = 1

        for index in range(1, len(s)):
            if ord(s[index]) == ord(s[index - 1]) + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)

        return longest
