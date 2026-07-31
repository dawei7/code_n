from heapq import heappop, heappush
from typing import List


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        answers = [-1] * len(queries)
        waiting = [[] for _ in heights]

        for query_index, (first, second) in enumerate(queries):
            if first > second:
                first, second = second, first

            if first == second or heights[first] < heights[second]:
                answers[query_index] = second
            else:
                waiting[second].append((heights[first], query_index))

        active = []
        for building, height in enumerate(heights):
            while active and active[0][0] < height:
                _, query_index = heappop(active)
                answers[query_index] = building

            for threshold, query_index in waiting[building]:
                heappush(active, (threshold, query_index))

        return answers
