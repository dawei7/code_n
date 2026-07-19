from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        characters = list(s)
        total_shift = 0

        for index in range(len(s) - 1, -1, -1):
            total_shift = (total_shift + shifts[index]) % 26
            alphabet_index = ord(s[index]) - ord("a")
            characters[index] = chr((alphabet_index + total_shift) % 26 + ord("a"))

        return "".join(characters)
