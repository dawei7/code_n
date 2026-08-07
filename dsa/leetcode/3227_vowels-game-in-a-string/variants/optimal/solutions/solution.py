class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(character in "aeiou" for character in s)
