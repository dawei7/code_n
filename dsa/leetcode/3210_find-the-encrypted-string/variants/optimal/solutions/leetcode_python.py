class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        offset = k % len(s)
        return s[offset:] + s[:offset]
