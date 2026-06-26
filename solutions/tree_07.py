"""
Description
-----------
Return the diameter of the tree — the longest path
between any two nodes, measured in EDGES. A single-node
tree has diameter 0. The tree is given in the same
multi-way shape as the other tree specs (children[i] is
the list of i's children); a path may go through any
node and use any number of children.
Requirement: O(n) — for each node, sum the two tallest
subtree depths; the diameter is the max of that sum.
Source: https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

Examples
--------
Example 1:
Input:  children = [[1, 2], [3, 4], [], [], []], root = 0, n = 5
Output: 3 (3-1-0-2 or 4-1-0-2)

Example 2:
Input:  children = [[1], [2], [3], []], root = 0, n = 4
Output: 3 (3-2-1-0)

Example 3:
Input:  children = [[]], root = 0, n = 1
Output: 0
"""

def solve(children, root, n):
    # Write your code here.
    return None
