"""Optimal app-local solution for LeetCode 863."""


def solve(root, target, k):
    parents = {root: None}
    target_node = None
    stack = [root]

    while stack:
        node = stack.pop()
        if node.val == target:
            target_node = node
        for child in (node.left, node.right):
            if child is not None:
                parents[child] = node
                stack.append(child)

    frontier = [target_node]
    visited = {target_node}

    for _ in range(k):
        next_frontier = []
        for node in frontier:
            for neighbor in (node.left, node.right, parents[node]):
                if neighbor is not None and neighbor not in visited:
                    visited.add(neighbor)
                    next_frontier.append(neighbor)
        frontier = next_frontier
        if not frontier:
            break

    return [node.val for node in frontier]
