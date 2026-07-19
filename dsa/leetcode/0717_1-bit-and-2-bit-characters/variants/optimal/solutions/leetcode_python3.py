from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0

        while index < len(bits) - 1:
            index += bits[index] + 1

        return index == len(bits) - 1
