"""Optimal solution for tree_18: Right Side View.

Return the list of node indices visible from the RIGHT
"""


def solve(children, root, n):
    """Right side view of a binary tree."""
    if root == -1:
        return []
    from collections import deque
    levels = []
    q = deque([(root, 0)])
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        if children[u][0] != -1:
            q.append((children[u][0], d + 1))
        if children[u][1] != -1:
            q.append((children[u][1], d + 1))
    return [level[-1] for level in levels]
