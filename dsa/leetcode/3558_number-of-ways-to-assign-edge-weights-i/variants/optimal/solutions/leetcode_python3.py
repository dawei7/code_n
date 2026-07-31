MODULUS = 1000000007


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        node_count = len(edges) + 1
        adjacency: list[list[int]] = [[] for _ in range(node_count + 1)]
        for first, second in edges:
            adjacency[first].append(second)
            adjacency[second].append(first)
        maximum_depth = 0
        stack = [(1, 0, 0)]
        while stack:
            node, parent, depth = stack.pop()
            maximum_depth = max(maximum_depth, depth)
            for neighbor in adjacency[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, depth + 1))
        return pow(2, maximum_depth - 1, MODULUS)
