from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        answer = 1
        for roll in rolls:
            seen.add(roll)
            if len(seen) == k:
                answer += 1
                seen.clear()
        return answer
