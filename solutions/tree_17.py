"""Solution for tree_17: Lowest Common Ancestor.


            Return the node index of the lowest common ancestor
            (LCA) of two nodes in a binary tree (not necessarily a BST).
            Walk the tree; the first node that's an ancestor of
            both is the LCA.
            Requirement: O(n) on a general tree, O(log n) on a BST.
            Source: https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
            

Inputs passed to solve():
    children: list of length n; children[i] = [left, right] (-1 = absent).
    root: the root node index.
    n: number of nodes.
    p: first node index.
    q: second node index.

Goal:
    the node index of the LCA of p and q.

Samples:
Sample 1 input:  children = [[1, 2], [3, 4], [-1, -1], [-1, -1], [-1, -1]], root = 0, n = 5, p = 3, q = 4
Sample 1 output: 1 (LCA of 3 and 4 is 1)

Sample 2 input:  children = [[1, 2], [-1, -1], [-1, -1]], root = 0, n = 3, p = 1, q = 2
Sample 2 output: 0 (root is the LCA)


"""

def solve(children, root, n, p, q):
    # Write your code here.
    return None
