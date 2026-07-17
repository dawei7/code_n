from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxAverageRatio(
        self,
        classes: List[List[int]],
        extraStudents: int,
    ) -> float:
        heap = [
            (-(total - passed) / (total * (total + 1)), passed, total)
            for passed, total in classes
        ]
        heapify(heap)

        for _ in range(extraStudents):
            _, passed, total = heappop(heap)
            passed += 1
            total += 1
            heappush(
                heap,
                (-(total - passed) / (total * (total + 1)), passed, total),
            )

        return sum(passed / total for _, passed, total in heap) / len(classes)
