"""Solution for tree_23: Kth Smallest in BST.

Return the kth smallest value in a BST (1-indexed).
In-order traversal visits the nodes in sorted order;
stop when we've seen k. O(n) worst case, O(h + k) if we
stop early.
Source: https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst/

Inputs passed to solve():
    children: list of length n; children[i] = [left, right].
    values: list of n values (parallel to children).
    root: the root node index.
    n: number of nodes.
    k: 1-indexed kth smallest.

Goal:
    the kth smallest value, or -1 if k is out of range.

Samples:
Sample 1 input:  children = [[1, 2], [-1, -1], [-1, -1]], root = 0, n = 3, k = 2
Sample 1 output: 2 (sorted: 1, 2, 3)


"""

def solve(children, values, root, n, k):
    # Write your code here.
    return None
