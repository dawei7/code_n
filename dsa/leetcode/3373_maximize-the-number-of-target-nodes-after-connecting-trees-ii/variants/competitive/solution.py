from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def color_tree(edges: List[List[int]]) -> tuple[List[int], List[int]]:
            node_count = len(edges) + 1
            graph = [[] for _ in range(node_count)]
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)

            parity = [-1] * node_count
            parity[0] = 0
            counts = [1, 0]
            stack = [0]

            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if parity[neighbor] == -1:
                        parity[neighbor] = parity[node] ^ 1
                        counts[parity[neighbor]] += 1
                        stack.append(neighbor)

            return parity, counts

        parity1, counts1 = color_tree(edges1)
        _, counts2 = color_tree(edges2)
        best_second_tree = max(counts2)

        return [counts1[color] + best_second_tree for color in parity1]
