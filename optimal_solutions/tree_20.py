"""Optimal solution for tree_20: Binary Tree to BST.

Convert a binary tree to a binary SEARCH tree holding the
same values. In-order walk to collect nodes; sort values;
walk in-order again, replacing each node's value with
the next sorted value.
"""


def solve(children, values, root, n):
    if n == 0 or root == -1:
        return [], []
    out = []

    def collect(i):
        if i == -1:
            return
        collect(children[i][0])
        out.append(i)
        collect(children[i][1])
    collect(root)
    sorted_vals = sorted(values)
    new_values = list(values)
    for idx, node in enumerate(out):
        new_values[node] = sorted_vals[idx]
    return list(children), new_values
