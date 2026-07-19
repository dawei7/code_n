from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        previous = set()
        answer = float("inf")

        for value in arr:
            current = {value}
            current.update(candidate & value for candidate in previous)
            for candidate in current:
                answer = min(answer, abs(candidate - target))
            if answer == 0:
                return 0
            previous = current

        return int(answer)
