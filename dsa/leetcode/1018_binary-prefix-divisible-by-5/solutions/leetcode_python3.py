from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        remainder = 0
        answer = []

        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            answer.append(remainder == 0)

        return answer
