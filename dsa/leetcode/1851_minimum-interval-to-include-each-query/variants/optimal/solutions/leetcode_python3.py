import heapq
from typing import List


class Solution:
    def minInterval(
        self, intervals: List[List[int]], queries: List[int]
    ) -> List[int]:
        intervals.sort()
        ordered_queries = sorted((value, index) for index, value in enumerate(queries))
        answers = [-1] * len(queries)
        active = []
        interval_index = 0

        for query, original_index in ordered_queries:
            while (
                interval_index < len(intervals)
                and intervals[interval_index][0] <= query
            ):
                left, right = intervals[interval_index]
                heapq.heappush(active, (right - left + 1, right))
                interval_index += 1

            while active and active[0][1] < query:
                heapq.heappop(active)

            if active:
                answers[original_index] = active[0][0]

        return answers
