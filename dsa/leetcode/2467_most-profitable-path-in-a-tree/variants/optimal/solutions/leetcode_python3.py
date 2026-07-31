from typing import List


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        node_count = len(amount)
        graph = [[] for _ in range(node_count)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        parent = [-2] * node_count
        parent[0] = -1
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                order.append(neighbor)

        bob_time = [node_count] * node_count
        node = bob
        time = 0
        while node != -1:
            bob_time[node] = time
            node = parent[node]
            time += 1

        best_income = -10**18
        stack = [(0, -1, 0, 0)]
        while stack:
            node, previous, time, income = stack.pop()
            if time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2

            if node != 0 and len(graph[node]) == 1:
                best_income = max(best_income, income)
                continue

            for neighbor in graph[node]:
                if neighbor != previous:
                    stack.append((neighbor, node, time + 1, income))

        return best_income
