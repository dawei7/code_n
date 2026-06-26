"""Optimal solution for tree_05: Level-Order Traversal.

BFS, return a list of lists — one row per depth.
"""


def solve(children, root, n):
    from collections import deque
    levels = []
    q = deque()
    q.append((root, 0))
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        for v in children[u]:
            q.append((v, d + 1))
    return levels
