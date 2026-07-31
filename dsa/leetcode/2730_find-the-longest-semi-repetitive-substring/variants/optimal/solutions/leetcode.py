class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        previous_pair = -1
        longest = 1

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                if previous_pair != -1:
                    left = previous_pair
                previous_pair = right
            longest = max(longest, right - left + 1)

        return longest
