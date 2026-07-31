class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            smaller = min(chars[left], chars[right])
            chars[left] = chars[right] = smaller
            left += 1
            right -= 1
        return "".join(chars)
