from typing import List


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adjacency = [[] for _ in range(n)]
        for first, second, weight in edges:
            adjacency[first].append((second, weight))
            adjacency[second].append((first, weight))

        levels = n.bit_length()
        ancestors = [[-1] * levels for _ in range(n)]
        depth = [0] * n
        prefix_counts = [[0] * 26 for _ in range(n)]

        stack = [(0, -1)]
        while stack:
            node, parent = stack.pop()
            for neighbor, weight in adjacency[node]:
                if neighbor == parent:
                    continue
                ancestors[neighbor][0] = node
                depth[neighbor] = depth[node] + 1
                prefix_counts[neighbor] = prefix_counts[node].copy()
                prefix_counts[neighbor][weight - 1] += 1
                stack.append((neighbor, node))

        for level in range(1, levels):
            for node in range(n):
                middle = ancestors[node][level - 1]
                if middle != -1:
                    ancestors[node][level] = ancestors[middle][level - 1]

        def lowest_common_ancestor(first: int, second: int) -> int:
            if depth[first] < depth[second]:
                first, second = second, first

            difference = depth[first] - depth[second]
            for level in range(levels):
                if difference & (1 << level):
                    first = ancestors[first][level]

            if first == second:
                return first

            for level in range(levels - 1, -1, -1):
                if ancestors[first][level] != ancestors[second][level]:
                    first = ancestors[first][level]
                    second = ancestors[second][level]
            return ancestors[first][0]

        answer = []
        for first, second in queries:
            ancestor = lowest_common_ancestor(first, second)
            path_length = depth[first] + depth[second] - 2 * depth[ancestor]
            largest_frequency = max(
                prefix_counts[first][weight] + prefix_counts[second][weight] - 2 * prefix_counts[ancestor][weight]
                for weight in range(26)
            )
            answer.append(path_length - largest_frequency)
        return answer
