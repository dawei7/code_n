"""Solution for tree_20: Binary Tree to BST.

Convert a binary tree to a binary SEARCH tree holding the
same values. In-order walk to collect nodes; sort values;
walk in-order again, replacing each node's value with
the next sorted value. O(n log n) for the sort.
Source: https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/

Inputs passed to solve():
    children: list of length n; children[i] = [left, right].
    values: list of length n; values[i] is the value at node i.
    root: the root node index.
    n: number of nodes.

Goal:
    (new_children, new_values) - the BST holding the same values.

Samples:
Sample 1 input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 7, 3], root = 0, n = 3
Sample 1 output: ([(1,2),(-1,-1),(-1,-1)], [5,3,7]) (in-order 7,3,5 -> sorted 3,5,7)


"""

def solve(children, values, root, n):
    # Write your code here.
    return None
