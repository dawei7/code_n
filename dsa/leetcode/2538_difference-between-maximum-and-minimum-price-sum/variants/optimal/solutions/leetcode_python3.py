from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        adjacency = [[] for _ in range(n)]
        for first, second in edges:
            adjacency[first].append(second)
            adjacency[second].append(first)

        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in adjacency[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                order.append(neighbor)

        with_endpoint = price[:]
        without_endpoint = [0] * n
        answer = 0

        for node in reversed(order):
            for child in adjacency[node]:
                if parent[child] != node:
                    continue
                answer = max(
                    answer,
                    with_endpoint[node] + without_endpoint[child],
                    without_endpoint[node] + with_endpoint[child],
                )
                with_endpoint[node] = max(
                    with_endpoint[node],
                    price[node] + with_endpoint[child],
                )
                without_endpoint[node] = max(
                    without_endpoint[node],
                    price[node] + without_endpoint[child],
                )

        return answer
