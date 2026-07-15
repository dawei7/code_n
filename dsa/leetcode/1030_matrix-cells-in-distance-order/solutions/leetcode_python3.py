from typing import List


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        buckets = [[] for _ in range(rows + cols - 1)]
        for row in range(rows):
            for col in range(cols):
                distance = abs(row - rCenter) + abs(col - cCenter)
                buckets[distance].append([row, col])

        return [cell for bucket in buckets for cell in bucket]

