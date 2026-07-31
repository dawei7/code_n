from heapq import heappop, heappush


class Solution:
    def minTimeMaxPower(
        self,
        n: int,
        edges: List[List[int]],
        power: int,
        cost: List[int],
        source: int,
        target: int,
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for node, neighbor, travel_time in edges:
            graph[node].append((neighbor, travel_time))

        infinity = 10**30
        best_time = [[infinity] * (power + 1) for _ in range(n)]
        best_time[source][power] = 0
        heap = [(0, source, power)]

        while heap:
            elapsed, node, remaining = heappop(heap)
            if elapsed != best_time[node][remaining]:
                continue
            if remaining < cost[node]:
                continue

            next_power = remaining - cost[node]
            for neighbor, travel_time in graph[node]:
                arrival = elapsed + travel_time
                if arrival < best_time[neighbor][next_power]:
                    best_time[neighbor][next_power] = arrival
                    heappush(heap, (arrival, neighbor, next_power))

        minimum_time = min(best_time[target])
        if minimum_time == infinity:
            return [-1, -1]

        maximum_power = max(
            remaining
            for remaining, elapsed in enumerate(best_time[target])
            if elapsed == minimum_time
        )
        return [minimum_time, maximum_power]
