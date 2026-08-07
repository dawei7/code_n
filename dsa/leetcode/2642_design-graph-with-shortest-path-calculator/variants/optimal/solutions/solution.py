from heapq import heappop, heappush


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adjacency = [[] for _ in range(n)]
        for source, target, cost in edges:
            self.adjacency[source].append((target, cost))

    def addEdge(self, edge: List[int]) -> None:
        source, target, cost = edge
        self.adjacency[source].append((target, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        distance = [float("inf")] * self.n
        distance[node1] = 0
        heap = [(0, node1)]

        while heap:
            cost, node = heappop(heap)
            if node == node2:
                return cost
            if cost != distance[node]:
                continue

            for neighbor, edge_cost in self.adjacency[node]:
                candidate = cost + edge_cost
                if candidate < distance[neighbor]:
                    distance[neighbor] = candidate
                    heappush(heap, (candidate, neighbor))

        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
