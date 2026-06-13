"""Optimal solution for tree_23: Kth Smallest in BST.

In-order traversal visits the nodes in sorted order.
"""


def solve(children, values, root, n, k):
    out = []

    def inorder(i):
        if i == -1:
            return
        inorder(children[i][0])
        out.append(values[i])
        inorder(children[i][1])

    inorder(root)
    if k < 1 or k > len(out):
        return -1
    return out[k - 1]
