class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = 0
        uppercase = 0

        for character in word:
            if 'a' <= character <= 'z':
                lowercase |= 1 << (ord(character) - ord('a'))
            else:
                uppercase |= 1 << (ord(character) - ord('A'))

        return (lowercase & uppercase).bit_count()
