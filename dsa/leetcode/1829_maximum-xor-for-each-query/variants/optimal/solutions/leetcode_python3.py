from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        current_xor = 0
        for value in nums:
            current_xor ^= value

        mask = (1 << maximumBit) - 1
        answer = []
        for value in reversed(nums):
            answer.append(current_xor ^ mask)
            current_xor ^= value
        return answer
