from typing import List


class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        min_x = min(x for x, _ in points)
        max_x = max(x for x, _ in points)
        min_y = min(y for _, y in points)
        max_y = max(y for _, y in points)

        answer = float("inf")
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                distances = sorted(
                    abs(x - origin_x) + abs(y - origin_y)
                    for origin_x, origin_y in points
                )
                answer = min(answer, distances[k - 1])

        return answer
