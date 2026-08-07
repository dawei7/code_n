class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        from heapq import heappop, heappush

        graph = [[] for _ in range(n)]
        for source, target, weight in edges:
            graph[source].append((target, weight))

        marked_nodes = set(marked)
        distances = [float("inf")] * n
        distances[s] = 0
        heap = [(0, s)]

        while heap:
            distance, node = heappop(heap)
            if distance != distances[node]:
                continue
            if node in marked_nodes:
                return distance

            for neighbor, weight in graph[node]:
                candidate = distance + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))

        return -1
