class Solution:
    def partitionString(self, s: str) -> int:
        partitions = 1
        used_letters = 0

        for letter in s:
            letter_bit = 1 << (ord(letter) - ord("a"))
            if used_letters & letter_bit:
                partitions += 1
                used_letters = 0
            used_letters |= letter_bit

        return partitions
