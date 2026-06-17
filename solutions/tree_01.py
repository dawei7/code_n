"""Solution for tree_01: Preorder Traversal.

Return the nodes of the tree in preorder:
visit the node, then recursively visit each child
subtree from left to right.
The tree is given as children[i] = list of i's children.
Requirement: O(n) where n is the number of nodes.
Source: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

Inputs passed to solve():
    children: list of length n; children[i] is the list of i's children.
    root: the root node index.
    n: number of nodes in the tree.

Goal:
    a list of node indices in preorder.

Samples:
Sample 1 input:  children = [[1, 2], [], []], root = 0, n = 3
Sample 1 output: [0, 1, 2]

Sample 2 input:  children = [[1], [2], []], root = 0, n = 3
Sample 2 output: [0, 1, 2]

Sample 3 input:  children = [[]], root = 0, n = 1
Sample 3 output: [0]

"""

def solve(children, root, n):
    # Write your code here.
    return None
