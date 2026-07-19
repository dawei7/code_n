def solve(n: int, corridors: list[list[int]]) -> int:
    neighbors = [set() for _ in range(n + 1)]
    for first, second in corridors:
        neighbors[first].add(second)
        neighbors[second].add(first)

    shared_neighbors = 0
    for first, second in corridors:
        shared_neighbors += len(neighbors[first] & neighbors[second])

    return shared_neighbors // 3
