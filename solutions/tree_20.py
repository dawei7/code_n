"""
Description
-----------
Convert a binary tree to a binary SEARCH tree holding the
same values. In-order walk to collect nodes; sort values;
walk in-order again, replacing each node's value with
the next sorted value. O(n log n) for the sort.
Source: https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/

Examples
--------
Example 1:
Input:  children = [[1, 2], [-1, -1], [-1, -1]], values = [5, 7, 3], root = 0, n = 3
Output: ([(1, 2), (-1, -1), (-1, -1)], [5, 3, 7]) (in-order 7, 3, 5 -> sorted 3, 5, 7)
"""

def solve(children, values, root, n):
    # Write your code here.
    return None
