"""Optimal solution for tree_08: BST Insert.

Walk a BST, insert at the first empty child slot.
"""


def solve(children, values, root, n, key):
    new_children = [list(c) for c in children]
    new_values = list(values)
    if n == 0:
        new_values.append(key)
        new_children.append([-1, -1])
        return new_children, new_values
    u = root
    while True:
        if key == new_values[u]:
            return new_children, new_values
        if key < new_values[u]:
            left, right = new_children[u]
            if left == -1:
                new_idx = len(new_values)
                new_values.append(key)
                new_children.append([-1, -1])
                new_children[u][0] = new_idx
                return new_children, new_values
            u = left
        else:
            left, right = new_children[u]
            if right == -1:
                new_idx = len(new_values)
                new_values.append(key)
                new_children.append([-1, -1])
                new_children[u][1] = new_idx
                return new_children, new_values
            u = right
