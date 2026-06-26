"""Optimal solution for tree_15: BST Delete.

Delete a key from a BST. The setup picks a key that is in
the tree; the canonical solve removes it. Three cases:
leaf (just drop), one child (replace with child), two
children (replace with inorder successor).

Tree is given as a binary shape: children[i] = [left, right]
where -1 means absent.
"""


def solve(children, values, root, n, key):
    """Delete `key` from the BST. Return (new_children, new_values)."""
    new_children = [list(c) for c in children]
    new_values = list(values)
    if n == 0:
        return new_children, new_values
    # Find the node to delete and its parent.
    u = root
    parent = -1
    while u != -1 and new_values[u] != key:
        parent = u
        u = new_children[u][0] if key < new_values[u] else new_children[u][1]
    if u == -1:
        return new_children, new_values  # not found
    left = new_children[u][0]
    right = new_children[u][1]
    if left == -1 and right == -1:
        # Leaf case.
        if parent == -1:
            return [], []
        if new_children[parent][0] == u:
            new_children[parent][0] = -1
        else:
            new_children[parent][1] = -1
    elif left == -1 or right == -1:
        # One child case.
        child = left if left != -1 else right
        if parent == -1:
            new_children[u] = [-1, -1]
        elif new_children[parent][0] == u:
            new_children[parent][0] = child
        else:
            new_children[parent][1] = child
    else:
        # Two children case: replace value with inorder successor
        # and unlink the successor.
        succ_parent = u
        succ = right
        while new_children[succ][0] != -1:
            succ_parent = succ
            succ = new_children[succ][0]
        new_values[u] = new_values[succ]
        if succ_parent == u:
            new_children[u][1] = new_children[succ][1]
        else:
            new_children[succ_parent][0] = new_children[succ][1]
    return new_children, new_values
