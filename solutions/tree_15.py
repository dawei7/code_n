"""
Description
-----------
Delete a key from a BST. The setup picks a key that
            is in the tree; the canonical solve removes it. Three
            cases: leaf (just drop), one child (replace with child),
            two children (replace with inorder successor).
            Tree is given as a binary shape: children[i] = [left, right].
            Requirement: O(log n) on a balanced BST.
            Source: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

Examples
--------
Example 1:
Input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 3, 7], root = 0, n = 3, key = 3
Output: ([(-1, 2), (-1, -1), (-1, -1)], [5, 7])

Example 2:
Input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 3, 7], root = 0, n = 3, key = 5
Output: ([(-1, 2), (-1, -1), (-1, -1)], [7, 3])
"""

def solve(children, values, root, n, key):
    # Write your code here.
    return None
