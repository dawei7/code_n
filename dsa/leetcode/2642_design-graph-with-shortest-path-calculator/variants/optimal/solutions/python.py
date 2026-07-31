from heapq import heappop, heappush


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.adjacency = [[] for _ in range(n)]
        for source, target, cost in edges:
            self.adjacency[source].append((target, cost))

    def addEdge(self, edge: list[int]) -> None:
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


def solve(operations: list[str], arguments: list[list]) -> list[int | None]:
    graph = None
    output = []
    for operation, args in zip(operations, arguments):
        if operation == "Graph":
            graph = Graph(args[0], args[1])
            output.append(None)
        elif operation == "addEdge":
            graph.addEdge(args[0])
            output.append(None)
        elif operation == "shortestPath":
            output.append(graph.shortestPath(args[0], args[1]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
