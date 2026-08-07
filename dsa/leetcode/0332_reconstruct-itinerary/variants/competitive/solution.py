from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destinations = defaultdict(list)
        for departure, arrival in tickets:
            destinations[departure].append(arrival)
        for arrivals in destinations.values():
            arrivals.sort(reverse=True)

        stack = ["JFK"]
        reversed_route = []
        while stack:
            current = stack[-1]
            if destinations[current]:
                stack.append(destinations[current].pop())
            else:
                reversed_route.append(stack.pop())
        return reversed_route[::-1]
