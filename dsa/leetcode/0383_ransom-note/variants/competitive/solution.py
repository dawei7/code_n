class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = [0] * 26
        base = ord("a")

        for character in magazine:
            available[ord(character) - base] += 1

        for character in ransomNote:
            index = ord(character) - base
            if available[index] == 0:
                return False
            available[index] -= 1

        return True
