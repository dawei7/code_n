class Solution:
    def maxKDivisibleComponents(
        self,
        n: int,
        edges: List[List[int]],
        values: List[int],
        k: int,
    ) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        remainders = [value % k for value in values]
        components = 0

        for node in reversed(order):
            if remainders[node] == 0:
                components += 1
            elif parent[node] != -1:
                remainders[parent[node]] = (remainders[parent[node]] + remainders[node]) % k

        return components
