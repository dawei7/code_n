import heapq


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))

        infinity = float("inf")
        distances = [infinity] * n
        distances[0] = 0
        heap = [(0, 0)]

        while heap:
            time, node = heapq.heappop(heap)
            if time != distances[node]:
                continue

            for neighbor, length in graph[node]:
                arrival = time + length
                if arrival < distances[neighbor] and arrival < disappear[neighbor]:
                    distances[neighbor] = arrival
                    heapq.heappush(heap, (arrival, neighbor))

        return [-1 if distance == infinity else distance for distance in distances]
