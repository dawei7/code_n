from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        answer = target[0]
        for previous, current in zip(target, target[1:]):
            if current > previous:
                answer += current - previous
        return answer
