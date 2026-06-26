"""Optimal solution for tree_16: Serialize / Deserialize.

Standard format: preorder traversal with 'N' for null,
comma-separated. The serialize-then-deserialize round-trip
preserves the structure on a valid binary tree. Deserialization
uses the original node indices from the tokens so the round-trip
is a structural identity.
"""


def solve(children, root, n):
    """Serialize the tree, then deserialize it. Return the new children list."""
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
    tokens = ",".join(parts).split(",")

    # Deserialize: pre-register each new node at the index named
    # by the token, then recurse on left/right.
    idx = [0]
    new_children = []

    def build():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node_idx = int(tok)
        while len(new_children) <= node_idx:
            new_children.append([-1, -1])
        new_children[node_idx][0] = build()
        new_children[node_idx][1] = build()
        return node_idx

    build()
    return new_children
