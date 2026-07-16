from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        positions = sorted(houses)
        house_count = len(positions)

        interval_cost = [[0] * house_count for _ in range(house_count)]
        for length in range(2, house_count + 1):
            for left in range(house_count - length + 1):
                right = left + length - 1
                inner_cost = 0
                if left + 1 <= right - 1:
                    inner_cost = interval_cost[left + 1][right - 1]
                interval_cost[left][right] = (
                    inner_cost + positions[right] - positions[left]
                )

        infinity = 10**18
        previous = [infinity] * (house_count + 1)
        previous[0] = 0

        for boxes in range(1, k + 1):
            current = [infinity] * (house_count + 1)

            for end in range(boxes, house_count + 1):
                for start in range(boxes - 1, end):
                    current[end] = min(
                        current[end],
                        previous[start] + interval_cost[start][end - 1],
                    )

            previous = current

        return previous[house_count]
