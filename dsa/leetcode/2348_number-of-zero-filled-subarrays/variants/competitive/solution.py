from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = run = 0
        for value in nums:
            run = run + 1 if value == 0 else 0
            answer += run
        return answer
