def solve(edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    node_count = len(edges) + 1
    graph: list[list[tuple[int, int]]] = [[] for _ in range(node_count)]
    for first, second, weight in edges:
        graph[first].append((second, weight))
        graph[second].append((first, weight))

    depth = [0] * node_count
    root_distance = [0] * node_count
    parent = [0] * node_count
    traversal = [0]
    for node in traversal:
        for neighbor, weight in graph[node]:
            if neighbor == parent[node]:
                continue
            parent[neighbor] = node
            depth[neighbor] = depth[node] + 1
            root_distance[neighbor] = root_distance[node] + weight
            traversal.append(neighbor)

    level_count = node_count.bit_length()
    ancestors = [parent]
    for _ in range(1, level_count):
        previous = ancestors[-1]
        ancestors.append([previous[previous[node]] for node in range(node_count)])

    def lowest_common_ancestor(first: int, second: int) -> int:
        if depth[first] < depth[second]:
            first, second = second, first

        difference = depth[first] - depth[second]
        for level in range(level_count):
            if difference & (1 << level):
                first = ancestors[level][first]

        if first == second:
            return first

        for level in range(level_count - 1, -1, -1):
            if ancestors[level][first] != ancestors[level][second]:
                first = ancestors[level][first]
                second = ancestors[level][second]
        return ancestors[0][first]

    def distance(first: int, second: int) -> int:
        ancestor = lowest_common_ancestor(first, second)
        return (
            root_distance[first]
            + root_distance[second]
            - 2 * root_distance[ancestor]
        )

    answer = []
    for first, second, destination in queries:
        pairwise_sum = (
            distance(first, second)
            + distance(first, destination)
            + distance(second, destination)
        )
        answer.append(pairwise_sum // 2)
    return answer
