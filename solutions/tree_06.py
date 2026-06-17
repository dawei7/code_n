"""Solution for tree_06: BST Search.

Search for `target` in a binary search tree. The tree is
given as a binary shape: children[i] = [left_index, right_index]
(either can be -1 for absent), plus values[i] for the value
at each node. Return the node index where target is found,
or -1 if it is not in the tree.
Requirement: O(log n) on a balanced BST (the setup inserts
in random order, so the tree may be unbalanced — worst
case O(n), but the spec advertises O(log n)).
Source: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

Inputs passed to solve():
    children: list of length n; children[i] = [left, right] (each -1 if absent).
    values: list of length n; values[i] is the BST key at node i.
    root: the root node index.
    n: number of nodes in the tree.
    target: the value to search for.

Goal:
    the node index where target is found, or -1 if not in the tree.

Samples:
Sample 1 input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [10, 5, 15], root = 0, n = 3, target = 15
Sample 1 output: 2

Sample 2 input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [10, 5, 15], root = 0, n = 3, target = 7
Sample 2 output: -1

Sample 3 input:  children = [[-1, -1]], values = [42], root = 0, n = 1, target = 42
Sample 3 output: 0

"""

def solve(children, values, root, n, target):
    # Write your code here.
    return None
