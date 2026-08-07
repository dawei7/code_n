from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        answer = 0
        previous = 0

        for rung in rungs:
            answer += (rung - previous - 1) // dist
            previous = rung

        return answer
