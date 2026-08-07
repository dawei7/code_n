class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        frequencies = [0] * 26
        total = 0

        for character in s:
            index = ord(character) - ord("a")
            frequencies[index] += 1
            total += frequencies[index]

        return total
