def solve(n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
    adjacency = [[] for _ in range(n)]
    for first, second in edges:
        adjacency[first].append(second)
        adjacency[second].append(first)
    usage = [0] * n

    def count_path(node: int, parent: int, target: int) -> bool:
        if node == target:
            usage[node] += 1
            return True
        for neighbor in adjacency[node]:
            if neighbor != parent and count_path(neighbor, node, target):
                usage[node] += 1
                return True
        return False

    for start, end in trips:
        count_path(start, -1, end)

    def minimize(node: int, parent: int) -> tuple[int, int]:
        full = usage[node] * price[node]
        halved = usage[node] * (price[node] // 2)
        for neighbor in adjacency[node]:
            if neighbor == parent:
                continue
            child_full, child_halved = minimize(neighbor, node)
            full += min(child_full, child_halved)
            halved += child_full
        return full, halved

    return min(minimize(0, -1))
