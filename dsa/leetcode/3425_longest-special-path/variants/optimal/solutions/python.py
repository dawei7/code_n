def solve(edges, nums):
    graph = [[] for _ in nums]
    for u, v, length in edges:
        graph[u].append((v, length))
        graph[v].append((u, length))

    best_length = 0
    best_nodes = 1
    path_distances = []
    last_depth = {}
    stack = [(0, 0, -1, 0, 0)]

    while stack:
        event, node, parent, distance, left = stack.pop()

        if event == 1:
            path_distances.pop()
            if distance == -1:
                del last_depth[node]
            else:
                last_depth[node] = distance
            continue

        depth = len(path_distances)
        path_distances.append(distance)
        value = nums[node]
        previous_depth = last_depth.get(value, -1)
        left = max(left, previous_depth + 1)

        length = distance - path_distances[left]
        nodes = depth - left + 1
        if length > best_length:
            best_length = length
            best_nodes = nodes
        elif length == best_length:
            best_nodes = min(best_nodes, nodes)

        last_depth[value] = depth
        stack.append((1, value, -1, previous_depth, 0))
        for neighbor, weight in reversed(graph[node]):
            if neighbor != parent:
                stack.append((0, neighbor, node, distance + weight, left))

    return [best_length, best_nodes]
