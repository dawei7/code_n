"""Optimal solution for tree_17: Lowest Common Ancestor.

Return the node index of the lowest common ancestor
"""


def solve(children, root, n, p, q):
    """Return the LCA of p and q in a binary tree."""
    if root == -1:
        return -1
    # Path from root to p.
    def path_to(u, target):
        if u == -1:
            return None
        if u == target:
            return [u]
        left = path_to(children[u][0], target)
        if left is not None:
            return [u] + left
        right = path_to(children[u][1], target)
        if right is not None:
            return [u] + right
        return None
    pp = path_to(root, p)
    pq = path_to(root, q)
    if pp is None or pq is None:
        return -1
    last = -1
    for a, b in zip(pp, pq):
        if a == b:
            last = a
        else:
            break
    return last
