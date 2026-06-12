"""Optimal solution for tree_19: Boundary Traversal.

Return the boundary traversal of a binary tree:
"""


def solve(children, root, n):
    """Boundary traversal: left edge, leaves, right edge (reversed)."""
    if root == -1:
        return []
    out = [root]

    def is_leaf(u):
        return children[u][0] == -1 and children[u][1] == -1

    def left_boundary(u):
        cur = children[u][0]
        while cur != -1:
            if not is_leaf(cur):
                out.append(cur)
            cur = children[cur][0] if children[cur][0] != -1 else children[cur][1]

    def leaves(u):
        if u == -1:
            return
        if is_leaf(u):
            out.append(u)
        else:
            leaves(children[u][0])
            leaves(children[u][1])

    def right_boundary(u):
        stack = []
        cur = children[u][1]
        while cur != -1:
            if not is_leaf(cur):
                stack.append(cur)
            cur = children[cur][1] if children[cur][1] != -1 else children[cur][0]
        while stack:
            out.append(stack.pop())

    if not is_leaf(root):
        left_boundary(root)
        leaves(root)
        right_boundary(root)
    # If root is a leaf, leaves() would only emit root; we
    # already added it. The contract: include the root exactly once.
    return out
