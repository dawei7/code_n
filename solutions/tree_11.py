"""Solution for tree_11: Balanced Tree Check.

Return True iff the binary tree is height-balanced:
for every node, the heights of its left and right
subtrees differ by at most 1.
Tree is given as a binary shape: children[i] = [left, right].
Requirement: O(n).
Source: https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/

Inputs passed to solve():
    children: list of length n; children[i] = [left, right] (-1 = absent).
    root: the root node index.
    n: number of nodes.

Goal:
    True iff the tree is height-balanced.

Samples:
Sample 1 input:  children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [-1, -1]], root = 0, n = 5
Sample 1 output: True

Sample 2 input:  children = [[1, -1], [-1, -1]], root = 0, n = 2
Sample 2 output: True

Sample 3 input:  children = [[1, 2], [-1, -1], [3, -1], [-1, -1], [-1, -1]], root = 0, n = 5
Sample 3 output: False

"""

def solve(children, root, n):
    # Write your code here.
    return None
