from collections import deque


def solve(edges1: list[list[int]], edges2: list[list[int]]) -> int:
    def diameter(edges: list[list[int]]) -> int:
        node_count = len(edges) + 1
        graph = [[] for _ in range(node_count)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        def farthest(start: int) -> tuple[int, int]:
            queue = deque([(start, -1, 0)])
            farthest_node = start
            farthest_distance = 0
            while queue:
                node, parent, distance = queue.popleft()
                if distance > farthest_distance:
                    farthest_node = node
                    farthest_distance = distance
                for neighbor in graph[node]:
                    if neighbor != parent:
                        queue.append((neighbor, node, distance + 1))
            return farthest_node, farthest_distance

        endpoint, _ = farthest(0)
        _, tree_diameter = farthest(endpoint)
        return tree_diameter

    first_diameter = diameter(edges1)
    second_diameter = diameter(edges2)
    merged_path = (first_diameter + 1) // 2 + (second_diameter + 1) // 2 + 1
    return max(first_diameter, second_diameter, merged_path)
