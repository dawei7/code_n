from typing import List


class Solution:
    def earliestFullBloom(
        self,
        plantTime: List[int],
        growTime: List[int],
    ) -> int:
        planted = 0
        answer = 0
        for growth, planting in sorted(
            zip(growTime, plantTime),
            reverse=True,
        ):
            planted += planting
            answer = max(answer, planted + growth)
        return answer
