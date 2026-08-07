from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        answer = 0

        for movement in nums:
            position += movement
            if position == 0:
                answer += 1

        return answer
