from typing import List
import heapq


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        roads = []
        for x1, y1, x2, y2, cost in specialRoads:
            cost = min(cost, abs(x2 - x1) + abs(y2 - y1))
            roads.append((x1, y1, x2, y2, cost))

        start_point = (start[0], start[1])
        distances = {start_point: 0}
        heap = [(0, start[0], start[1])]
        answer = abs(target[0] - start[0]) + abs(target[1] - start[1])

        while heap:
            cost, x, y = heapq.heappop(heap)
            if cost != distances.get((x, y)):
                continue

            answer = min(answer, cost + abs(target[0] - x) + abs(target[1] - y))

            for x1, y1, x2, y2, road_cost in roads:
                next_cost = cost + abs(x1 - x) + abs(y1 - y) + road_cost
                end = (x2, y2)
                if next_cost < distances.get(end, float("inf")):
                    distances[end] = next_cost
                    heapq.heappush(heap, (next_cost, x2, y2))

        return answer
