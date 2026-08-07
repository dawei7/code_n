class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for source, target in edges:
            graph[source].append((target, 0))
            graph[target].append((source, 1))

        parent = [-2] * n
        parent[0] = -1
        incoming_cost = [0] * n
        order = [0]
        root_cost = 0

        for node in order:
            for neighbor, cost in graph[node]:
                if parent[neighbor] != -2:
                    continue
                parent[neighbor] = node
                incoming_cost[neighbor] = cost
                root_cost += cost
                order.append(neighbor)

        answer = [0] * n
        answer[0] = root_cost
        for node in order[1:]:
            answer[node] = answer[parent[node]] + 1 - 2 * incoming_cost[node]

        return answer
