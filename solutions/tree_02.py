"""Solution for tree_02: Inorder Traversal.

Return the nodes of the tree in inorder (multi-way form):
recurse on the first child subtree, then visit the
node, then recurse on each remaining child subtree.
Requirement: O(n).
Source: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

Inputs passed to solve():
    children: list of length n; children[i] is the list of i's children.
    root: the root node index.
    n: number of nodes in the tree.

Goal:
    a list of node indices in inorder.

Samples:
Sample 1 input:  children = [[1, 2], [], []], root = 0, n = 3
Sample 1 output: [1, 0, 2]

Sample 2 input:  children = [[]], root = 0, n = 1
Sample 2 output: [0]


"""

def solve(children, root, n):
    # Write your code here.
    return None
