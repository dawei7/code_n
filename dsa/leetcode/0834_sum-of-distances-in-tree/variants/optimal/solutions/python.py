"""Optimal app-local solution for LeetCode 834."""


def solve(n, edges):
    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    parent = [-1] * n
    parent[0] = 0
    depth = [0] * n
    order = [0]

    for node in order:
        for neighbor in graph[node]:
            if neighbor == parent[node]:
                continue
            parent[neighbor] = node
            depth[neighbor] = depth[node] + 1
            order.append(neighbor)

    subtree_size = [1] * n
    for node in reversed(order[1:]):
        subtree_size[parent[node]] += subtree_size[node]

    answer = [0] * n
    answer[0] = sum(depth)
    for node in order[1:]:
        answer[node] = answer[parent[node]] + n - 2 * subtree_size[node]

    return answer
