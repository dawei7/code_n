class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        characters = set(s)
        for index, character in enumerate(s):
            if character.swapcase() not in characters:
                left = self.longestNiceSubstring(s[:index])
                right = self.longestNiceSubstring(s[index + 1 :])
                return left if len(left) >= len(right) else right

        return s
