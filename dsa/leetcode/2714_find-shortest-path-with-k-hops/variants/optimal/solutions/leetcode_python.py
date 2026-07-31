from heapq import heappop, heappush


class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for first, second, weight in edges:
            graph[first].append((second, weight))
            graph[second].append((first, weight))

        distances = [[float("inf")] * (k + 1) for _ in range(n)]
        distances[s][0] = 0
        heap = [(0, s, 0)]

        while heap:
            distance, node, hops = heappop(heap)
            if distance != distances[node][hops]:
                continue
            if node == d:
                return distance

            for neighbor, weight in graph[node]:
                paid_distance = distance + weight
                if paid_distance < distances[neighbor][hops]:
                    distances[neighbor][hops] = paid_distance
                    heappush(heap, (paid_distance, neighbor, hops))

                if hops < k and distance < distances[neighbor][hops + 1]:
                    distances[neighbor][hops + 1] = distance
                    heappush(heap, (distance, neighbor, hops + 1))

        return -1

