import sys

sys.setrecursionlimit(200000)


def solve(edges, nums):
    n = len(nums)
    graph = [[] for _ in range(n)]
    for u, v, length in edges:
        graph[u].append((v, length))
        graph[v].append((u, length))

    best_length = 0
    best_nodes = 1
    last_depth = {}

    def dfs(node, parent, depth, distance, left_depth, path_distances):
        nonlocal best_length, best_nodes

        value = nums[node]
        previous_depth = last_depth.get(value, -1)
        current_left = max(left_depth, previous_depth + 1)
        length = distance - path_distances[current_left]
        node_count = depth - current_left + 1

        if length > best_length:
            best_length = length
            best_nodes = node_count
        elif length == best_length:
            best_nodes = min(best_nodes, node_count)

        old_depth = last_depth.get(value)
        last_depth[value] = depth

        for child, edge_length in graph[node]:
            if child == parent:
                continue
            path_distances.append(distance + edge_length)
            dfs(child, node, depth + 1, distance + edge_length, current_left, path_distances)
            path_distances.pop()

        if old_depth is None:
            del last_depth[value]
        else:
            last_depth[value] = old_depth

    dfs(0, -1, 0, 0, 0, [0])
    return [best_length, best_nodes]
