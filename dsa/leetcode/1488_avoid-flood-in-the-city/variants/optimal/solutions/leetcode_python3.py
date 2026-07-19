from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        future = defaultdict(deque)
        for day, lake in enumerate(rains):
            if lake > 0:
                future[lake].append(day)

        full = set()
        current_deadline = {}
        deadlines = []
        result = [1] * len(rains)

        for day, lake in enumerate(rains):
            if lake > 0:
                result[day] = -1
                future[lake].popleft()

                if lake in full:
                    return []

                full.add(lake)
                if future[lake]:
                    deadline = future[lake][0]
                    current_deadline[lake] = deadline
                    heappush(deadlines, (deadline, lake))
                else:
                    current_deadline.pop(lake, None)
                continue

            while deadlines:
                deadline, urgent_lake = deadlines[0]
                if (
                    urgent_lake in full
                    and current_deadline.get(urgent_lake) == deadline
                ):
                    break
                heappop(deadlines)

            if deadlines:
                _, urgent_lake = heappop(deadlines)
                full.remove(urgent_lake)
                current_deadline.pop(urgent_lake, None)
                result[day] = urgent_lake

        return result
