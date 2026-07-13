class Solution:
    def longestPalindrome(self, s: str) -> int:
        unmatched = set()
        length = 0

        for character in s:
            if character in unmatched:
                unmatched.remove(character)
                length += 2
            else:
                unmatched.add(character)

        return length + bool(unmatched)
