"""Solution for tree_12: Symmetric Tree Check.

Return True iff the binary tree is symmetric around
its center: the left subtree is the mirror of the right
subtree.
Tree is given as a binary shape: children[i] = [left, right].
Requirement: O(n).
Source: https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/

Inputs passed to solve():
    children: list of length n; children[i] = [left, right] (-1 = absent).
    root: the root node index.
    n: number of nodes.

Goal:
    True iff the tree is symmetric around its root.

Samples:
Sample 1 input:  children = [[1, 2], [3, 4], [4, 3], [-1, -1], [-1, -1]], root = 0, n = 5
Sample 1 output: True

Sample 2 input:  children = [[1, -1], [-1, -1]], root = 0, n = 2
Sample 2 output: True

Sample 3 input:  children = [[1, 2], [3, -1], [-1, -1]], root = 0, n = 3
Sample 3 output: False

"""

def solve(children, root, n):
    # Write your code here.
    return None
