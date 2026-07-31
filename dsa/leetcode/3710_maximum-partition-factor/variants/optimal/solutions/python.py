def solve(points: list[list[int]]) -> int:
    n = len(points)
    if n == 2:
        return 0

    edges: list[tuple[int, int, int]] = []
    for first in range(n):
        x_first, y_first = points[first]
        for second in range(first + 1, n):
            x_second, y_second = points[second]
            distance = abs(x_first - x_second) + abs(y_first - y_second)
            edges.append((distance, first, second))
    edges.sort()

    parent = list(range(n))
    size = [1] * n
    parity = [0] * n

    def find(node: int) -> int:
        if parent[node] != node:
            previous = parent[node]
            parent[node] = find(previous)
            parity[node] ^= parity[previous]
        return parent[node]

    for distance, first, second in edges:
        root_first = find(first)
        root_second = find(second)
        first_parity = parity[first]
        second_parity = parity[second]

        if root_first == root_second:
            if first_parity == second_parity:
                return distance
            continue

        if size[root_first] > size[root_second]:
            root_first, root_second = root_second, root_first
            first_parity, second_parity = second_parity, first_parity

        parent[root_first] = root_second
        parity[root_first] = first_parity ^ second_parity ^ 1
        size[root_second] += size[root_first]

    return 0
