class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(left) - ord(right)) for left, right in zip(s, s[1:]))
