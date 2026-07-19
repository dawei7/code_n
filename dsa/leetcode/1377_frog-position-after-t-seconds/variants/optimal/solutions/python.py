"""Reference solution for LeetCode 1377."""


def solve(
    n: int,
    edges: list[list[int]],
    t: int,
    target: int,
) -> float:
    neighbors = [[] for _ in range(n + 1)]
    for first, second in edges:
        neighbors[first].append(second)
        neighbors[second].append(first)

    stack = [(1, 0, 0, 1.0)]
    while stack:
        node, parent, elapsed, probability = stack.pop()
        children = len(neighbors[node]) - (parent != 0)

        if node == target:
            if elapsed == t or children == 0:
                return probability
            return 0.0

        if elapsed == t or children == 0:
            continue

        next_probability = probability / children
        for adjacent in neighbors[node]:
            if adjacent != parent:
                stack.append((adjacent, node, elapsed + 1, next_probability))

    return 0.0
