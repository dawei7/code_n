def solve(edges: list[list[int]]) -> int:
    node_count = len(edges) + 1
    graph = [[] for _ in range(node_count)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    parent = [-1] * node_count
    order = [0]
    for node in order:
        for neighbor in graph[node]:
            if neighbor != parent[node]:
                parent[neighbor] = node
                order.append(neighbor)

    subtree_size = [1] * node_count
    good_nodes = 0
    for node in reversed(order):
        common_child_size = None
        is_good = True
        for neighbor in graph[node]:
            if parent[neighbor] == node:
                child_size = subtree_size[neighbor]
                if common_child_size is None:
                    common_child_size = child_size
                elif child_size != common_child_size:
                    is_good = False
                subtree_size[node] += child_size
        good_nodes += is_good

    return good_nodes
