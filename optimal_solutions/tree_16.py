"""Optimal solution for tree_16: Serialize / Deserialize.

Serialize a binary tree to a string, then deserialize it back.
"""


def solve(children, root, n):
    """Serialize the tree to a string, then deserialize it. Return the new children list."""
    # Serialize: preorder with 'N' for null.
    parts = []

    def ser(u):
        if u == -1:
            parts.append("N")
            return
        parts.append(str(u))
        ser(children[u][0])
        ser(children[u][1])

    ser(root)
    s = ",".join(parts)
    # Deserialize.
    tokens = s.split(",")
    idx = [0]

    def des():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node = int(tok)
        left = des()
        right = des()
        return [node, left, right]

    new_children = []
    nodes = []

    def build():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node_idx = len(nodes)
        nodes.append(int(tok))
        # Pre-register so children can refer to this index.
        new_children.append([-1, -1])
        new_children[node_idx][0] = build()
        new_children[node_idx][1] = build()
        return node_idx

    # Reset and rebuild.
    idx[0] = 0
    new_children = []
    new_root = build()
    return new_children
