def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    for first, second, weight in edges:
        graph[first].append((second, weight))
        graph[second].append((first, weight))

    levels = n.bit_length()
    parent = [0] * n
    depth = [0] * n
    distance = [0] * n
    stack = [(0, -1)]

    while stack:
        node, previous_node = stack.pop()
        for neighbor, weight in graph[node]:
            if neighbor == previous_node:
                continue
            parent[neighbor] = node
            depth[neighbor] = depth[node] + 1
            distance[neighbor] = distance[node] + weight
            stack.append((neighbor, node))

    up = [parent]
    for _ in range(1, levels):
        previous = up[-1]
        up.append([previous[previous[node]] for node in range(n)])

    def lca(first: int, second: int) -> int:
        if depth[first] < depth[second]:
            first, second = second, first

        difference = depth[first] - depth[second]
        for bit in range(levels):
            if difference >> bit & 1:
                first = up[bit][first]

        if first == second:
            return first

        for bit in range(levels - 1, -1, -1):
            if up[bit][first] != up[bit][second]:
                first = up[bit][first]
                second = up[bit][second]

        return up[0][first]

    answer = []
    for first, second in queries:
        if first == second:
            answer.append(first)
            continue

        common = lca(first, second)
        first_weight = distance[first] - distance[common]
        second_weight = distance[second] - distance[common]
        total = first_weight + second_weight

        if 2 * first_weight >= total:
            node = first
            for bit in range(levels - 1, -1, -1):
                candidate = up[bit][node]
                if 2 * (distance[first] - distance[candidate]) < total:
                    node = candidate
            answer.append(up[0][node])
        else:
            required = total - 2 * first_weight
            node = second
            for bit in range(levels - 1, -1, -1):
                candidate = up[bit][node]
                if depth[candidate] >= depth[common] and 2 * (distance[candidate] - distance[common]) >= required:
                    node = candidate
            answer.append(node)

    return answer
