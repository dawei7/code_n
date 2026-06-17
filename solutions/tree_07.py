"""Solution for tree_07: Tree Diameter.

Return the diameter of the tree — the longest path
between any two nodes, measured in EDGES. A single-node
tree has diameter 0. The tree is given in the same
multi-way shape as the other tree specs (children[i] is
the list of i's children); a path may go through any
node and use any number of children.
Requirement: O(n) — for each node, sum the two tallest
subtree depths; the diameter is the max of that sum.
Source: https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

Inputs passed to solve():
    children: list of length n; children[i] is the list of i's children.
    root: the root node index.
    n: number of nodes in the tree.

Goal:
    the tree diameter in edges (single node = 0).

Samples:
Sample 1 input:  children = [[1, 2], [3, 4], [], [], []], root = 0, n = 5
Sample 1 output: 3 (3-1-0-2 or 4-1-0-2)

Sample 2 input:  children = [[1], [2], [3], []], root = 0, n = 4
Sample 2 output: 3 (3-2-1-0)

Sample 3 input:  children = [[]], root = 0, n = 1
Sample 3 output: 0

"""

def solve(children, root, n):
    # Write your code here.
    return None
