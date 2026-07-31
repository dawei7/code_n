class Solution:
    def closestNode(
        self,
        n: int,
        edges: List[List[int]],
        query: List[List[int]],
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        levels = n.bit_length()
        parent = [[0] * n for _ in range(levels)]
        depth = [0] * n
        stack = [(0, -1)]

        while stack:
            node, previous = stack.pop()
            parent[0][node] = node if previous == -1 else previous
            for neighbor in graph[node]:
                if neighbor == previous:
                    continue
                depth[neighbor] = depth[node] + 1
                stack.append((neighbor, node))

        for level in range(1, levels):
            for node in range(n):
                parent[level][node] = parent[level - 1][
                    parent[level - 1][node]
                ]

        def lca(first: int, second: int) -> int:
            if depth[first] < depth[second]:
                first, second = second, first

            difference = depth[first] - depth[second]
            for level in range(levels):
                if difference >> level & 1:
                    first = parent[level][first]

            if first == second:
                return first

            for level in range(levels - 1, -1, -1):
                if parent[level][first] != parent[level][second]:
                    first = parent[level][first]
                    second = parent[level][second]

            return parent[0][first]

        answer = []
        for start, end, node in query:
            candidates = (
                lca(start, end),
                lca(start, node),
                lca(end, node),
            )
            answer.append(max(candidates, key=depth.__getitem__))

        return answer
