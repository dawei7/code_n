"""Solution for tree_05: Level-Order Traversal.

Return the nodes of the tree grouped by depth (BFS):
a list of lists where the d-th inner list is the nodes
at depth d. The root is at depth 0.
Requirement: O(n).
Source: https://www.geeksforgeeks.org/level-order-tree-traversal/

Inputs passed to solve():
    children: list of length n; children[i] is the list of i's children.
    root: the root node index.
    n: number of nodes in the tree.

Goal:
    a list of lists — one inner list per depth, in BFS order.

Samples:
Sample 1 input:  children = [[1, 2], [], []], root = 0, n = 3
Sample 1 output: [[0], [1], [2]]

Sample 2 input:  children = [[1, 2], [3], [4], [], []], root = 0, n = 5
Sample 2 output: [[0], [1, 2], [3, 4]]

Sample 3 input:  children = [[]], root = 0, n = 1
Sample 3 output: [[0]]

"""

def solve(children, root, n):
    # Write your code here.
    return None
