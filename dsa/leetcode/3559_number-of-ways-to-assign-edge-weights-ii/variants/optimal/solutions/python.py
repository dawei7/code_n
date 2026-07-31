MODULUS = 1_000_000_007


def solve(edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    node_count = len(edges) + 1
    level_count = node_count.bit_length()
    adjacency: list[list[int]] = [[] for _ in range(node_count)]
    for first, second in edges:
        first -= 1
        second -= 1
        adjacency[first].append(second)
        adjacency[second].append(first)

    depth = [0] * node_count
    ancestor = [[0] * node_count]
    stack = [(0, -1)]
    while stack:
        node, parent = stack.pop()
        for neighbor in adjacency[node]:
            if neighbor != parent:
                depth[neighbor] = depth[node] + 1
                ancestor[0][neighbor] = node
                stack.append((neighbor, node))

    for _ in range(1, level_count):
        previous = ancestor[-1]
        ancestor.append([previous[previous[node]] for node in range(node_count)])

    answers: list[int] = []
    for first, second in queries:
        first -= 1
        second -= 1
        original_depth_sum = depth[first] + depth[second]

        if depth[first] < depth[second]:
            first, second = second, first
        difference = depth[first] - depth[second]
        for level in range(level_count):
            if difference >> level & 1:
                first = ancestor[level][first]

        if first != second:
            for level in range(level_count - 1, -1, -1):
                if ancestor[level][first] != ancestor[level][second]:
                    first = ancestor[level][first]
                    second = ancestor[level][second]
            first = ancestor[0][first]

        distance = original_depth_sum - 2 * depth[first]
        answers.append(0 if distance == 0 else pow(2, distance - 1, MODULUS))

    return answers
