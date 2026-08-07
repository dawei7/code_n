from typing import List
import heapq


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        nearest = []
        answer = []

        for x, y in queries:
            heapq.heappush(nearest, -(abs(x) + abs(y)))
            if len(nearest) > k:
                heapq.heappop(nearest)

            answer.append(-nearest[0] if len(nearest) == k else -1)

        return answer
