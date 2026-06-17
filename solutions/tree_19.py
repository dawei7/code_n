"""Solution for tree_19: Boundary Traversal.


            Return the boundary traversal of a binary tree:
            left boundary (root-to-leaf, no leaves), then all leaves
            left-to-right, then right boundary (leaf-to-root, no leaves)
            in reverse. Avoid duplicates when the root is also a leaf.
            Requirement: O(n).
            Source: https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/
            

Inputs passed to solve():
    children: list of length n; children[i] = [left, right] (-1 = absent).
    root: the root node index.
    n: number of nodes.

Goal:
    list of node indices in boundary order.

Samples:
Sample 1 input:  children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [5, -1], [-1, -1]], root = 0, n = 6
Sample 1 output: [0, 1, 3, 5, 2, 4]


"""

def solve(children, root, n):
    # Write your code here.
    return None
