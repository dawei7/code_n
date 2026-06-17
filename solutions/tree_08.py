"""Solution for tree_08: BST Insert.

Insert `key` into a binary search tree. Return a tuple
(new_children, new_values) representing the BST after
the insert. If `key` is already in the tree, return
the tree unchanged.
The tree is given as a binary shape: children[i] = [left, right].
Requirement: O(log n) on a balanced BST.
Source: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

Inputs passed to solve():
    children: list of length n; children[i] = [left, right] (each -1 if absent).
    values: list of length n; values[i] is the BST key at node i.
    root: the root node index.
    n: number of nodes in the tree.
    key: the value to insert.

Goal:
    a tuple (new_children, new_values) of the BST after insert.

Samples:
Sample 1 input:  children = [[1, -1], [-1, -1]], values = [10, 5], root = 0, n = 2, key = 15
Sample 1 output: ([(1,2),(-1,-1),(-1,-1)], [10,5,15]) (added as right child of 10)

Sample 2 input:  children = [[1, -1], [-1, -1]], values = [10, 5], root = 0, n = 2, key = 10
Sample 2 output: unchanged (already in tree)


"""

def solve(children, values, root, n, key):
    # Write your code here.
    return None
