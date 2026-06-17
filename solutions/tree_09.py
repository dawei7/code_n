"""Solution for tree_09: Mirror Tree.

Return the children list of the mirrored (inverted) tree.
For a multi-way tree, mirroring means reversing every
node's child list. A single-node tree is its own mirror.
Requirement: O(n).
Source: https://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/

Inputs passed to solve():
    children: list of length n; children[i] is the list of i's children.
    root: the root node index.
    n: number of nodes in the tree.

Goal:
    a new children list with every node's child list reversed.

Samples:
Sample 1 input:  children = [[1, 2], [3, 4], [], [], []], root = 0, n = 5
Sample 1 output: [[2, 1], [4, 3], [], [], []]

Sample 2 input:  children = [[]], root = 0, n = 1
Sample 2 output: [[]]


"""

def solve(children, root, n):
    # Write your code here.
    return None
