from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}
        prefix = 0
        answer = 0

        for number in nums:
            prefix += number
            if prefix - target in seen:
                answer += 1
                seen = {0}
                prefix = 0
            else:
                seen.add(prefix)

        return answer

