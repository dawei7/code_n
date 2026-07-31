class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        parent = [-1] * n
        parent[0] = 0
        order = [0]
        for node in order:
            for neighbor, _ in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                order.append(neighbor)

        without_parent = [0] * n
        with_parent = [0] * n
        for node in reversed(order):
            base = 0
            gains = []
            for child, weight in graph[node]:
                if parent[child] != node:
                    continue
                base += without_parent[child]
                gains.append(weight + with_parent[child] - without_parent[child])

            gains.sort(reverse=True)
            without_parent[node] = base + sum(gain for gain in gains[:k] if gain > 0)
            with_parent[node] = base + sum(gain for gain in gains[: k - 1] if gain > 0)

        return without_parent[0]
