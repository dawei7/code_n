from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        answer = []
        for value in nums:
            if value in seen:
                answer.append(value)
            else:
                seen.add(value)
        return answer
