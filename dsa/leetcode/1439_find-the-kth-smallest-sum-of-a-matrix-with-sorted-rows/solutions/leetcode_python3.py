import heapq
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        sums = [0]
        for row in mat:
            heap = [
                (base + row[0], index, 0)
                for index, base in enumerate(sums)
            ]
            heapq.heapify(heap)
            merged = []
            while heap and len(merged) < k:
                value, sum_index, column = heapq.heappop(heap)
                merged.append(value)
                if column + 1 < len(row):
                    heapq.heappush(
                        heap,
                        (
                            sums[sum_index] + row[column + 1],
                            sum_index,
                            column + 1,
                        ),
                    )
            sums = merged
        return sums[k - 1]
