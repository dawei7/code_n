"""
Description
-----------
Search for target in a binary search tree. The tree is
given as a binary shape: children[i] = [left_index, right_index]
(either can be -1 for absent), plus values[i] for the value
at each node. Return the node index where target is found,
or -1 if it is not in the tree.
Requirement: O(log n) on a balanced BST (the setup inserts
in random order, so the tree may be unbalanced — worst
case O(n), but the spec advertises O(log n)).
Source: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

Examples
--------
Example 1:
Input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [10, 5, 15], root = 0, n = 3, target = 15
Output: 2

Example 2:
Input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [10, 5, 15], root = 0, n = 3, target = 7
Output: -1

Example 3:
Input:  children = [[-1, -1]], values = [42], root = 0, n = 1, target = 42
Output: 0
"""

def solve(children, values, root, n, target):
    # Write your code here.
    return None
