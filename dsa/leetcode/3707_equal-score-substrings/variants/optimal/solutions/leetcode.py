class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(char) - ord("a") + 1 for char in s)
        left = 0

        for char in s[:-1]:
            left += ord(char) - ord("a") + 1
            if left * 2 == total:
                return True

        return False
