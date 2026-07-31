class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        parent = [-1] * n
        parent[0] = 0
        children = [[] for _ in range(n)]
        order = [0]

        for node in order:
            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue

                parent[neighbor] = node
                children[node].append(neighbor)
                order.append(neighbor)

        best_path = [0] * n
        changed_nodes = 0

        for node in reversed(order):
            if not children[node]:
                best_path[node] = cost[node]
                continue

            target = max(best_path[child] for child in children[node])

            for child in children[node]:
                if best_path[child] < target:
                    changed_nodes += 1

            best_path[node] = cost[node] + target

        return changed_nodes
