def solve(root) -> int:
    nodes = [root]
    adjacency: list[list[int]] = [[]]

    for parent, node in enumerate(nodes):
        for child_node in (node.left, node.right):
            if child_node is None:
                continue

            child = len(nodes)
            nodes.append(child_node)
            adjacency.append([parent])
            adjacency[parent].append(child)

    answer = nodes[0].val

    for start in range(len(nodes)):
        seen: set[int] = set()
        stack = [(start, -1, 0, False)]

        while stack:
            node, parent, path_sum, exiting = stack.pop()
            value = nodes[node].val

            if exiting:
                seen.remove(value)
                continue

            if value in seen:
                continue

            path_sum += value
            answer = max(answer, path_sum)
            seen.add(value)
            stack.append((node, parent, path_sum, True))

            for neighbor in adjacency[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, path_sum, False))

    return answer
