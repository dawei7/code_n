"""Solution for tree_21: Root-to-Leaf Paths.

Return every root-to-leaf path as a list of node-index
lists. DFS from the root, accumulating the path; record
a copy when a leaf is reached. O(n) total.
Source: https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/

Inputs passed to solve():
    children: list of length n; children[i] = [left, right].
    root: the root node index (always 0 in the setup).
    n: number of nodes.

Goal:
    a list of paths; each path is a list of node indices.

Samples:
Sample 1 input:  children = [[1, 2], [3, -1], [-1, -1], [-1, -1]], root = 0, n = 4
Sample 1 output: [[0, 1, 3], [0, 2]]


"""

def solve(children, root, n):
    # Write your code here.
    return None
