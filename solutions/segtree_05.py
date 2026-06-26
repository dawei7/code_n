"""
Description
-----------
Build a sum-segment tree, then apply a sequence
            of range updates (add val to every element in
            [l, r]) using lazy propagation: when a node is
            fully inside the update range, add val * width
            to that node's sum and remember the pending
            update in a parallel lazy array (to be pushed
            down only when needed). Then for each query
            (l, r), return the range sum (with lazy tags
            pushed down on the way). O(log n) per op.
            Source: https://www.geeksforgeeks.org/dsa/lazy-propagation-in-segment-tree/

Examples
--------
Example 1:
Input:  arr = [1, 3, 5, 7, 9, 11], n = 6, range_updates = [(1, 3, 5)], queries = [(0, 5)], q = 1
Output: [46] ( = 1+8+10+12+9+11)

Example 2:
Input:  arr = [1, 2, 3], n = 3, range_updates = [(0, 2, 10)], queries = [(0, 0), (1, 2), (0, 2)], q = 3
Output: [11, 25, 36]
"""

def solve(arr, n, range_updates, queries, q):
    # Write your code here.
    return None
