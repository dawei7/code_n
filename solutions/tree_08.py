"""
Description
-----------
Insert key into a binary search tree. Return a tuple
(new_children, new_values) representing the BST after
the insert. If key is already in the tree, return
the tree unchanged.
The tree is given as a binary shape: children[i] = [left, right].
Requirement: O(log n) on a balanced BST.
Source: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

Examples
--------
Example 1:
Input:  children = [[1, -1], [-1, -1]], values = [10, 5], root = 0, n = 2, key = 15
Output: ([(1, 2), (-1, -1), (-1, -1)], [10, 5, 15]) (added as right child of 10)

Example 2:
Input:  children = [[1, -1], [-1, -1]], values = [10, 5], root = 0, n = 2, key = 10
Output: unchanged (already in tree)
"""

def solve(children, values, root, n, key):
    # Write your code here.
    return None
