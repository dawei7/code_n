"""
Description
-----------
Maintain an array of n integers under repeated
            range-add updates (add val to every element in
            the range [l, r]) and point queries (return the
            current value at index idx). The classic BIT
            trick: maintain a single BIT, add val at index
            l and subtract val at index r+1. The point
            query at idx is then the prefix sum [0, idx].
            O(log n) per update and per query.
            Source: https://www.geeksforgeeks.org/dsa/binary-indexed-tree-range-update-point-query/

Examples
--------
Example 1:
Input:  arr = [0, 0, 0, 0, 0], n = 5, range_updates = [(1, 3, 5)], point_queries = [(0, ), (1, ), (2, ), (3, ), (4, )], q = 5
Output: [0, 5, 5, 5, 0]

Example 2:
Input:  arr = [1, 3, 5, 7], n = 4, range_updates = [(0, 2, 10), (2, 3, -3)], point_queries = [(0, ), (1, ), (2, ), (3, )], q = 4
Output: [11, 13, 12, 4]
"""

def solve(arr, n, range_updates, point_queries, q):
    # Write your code here.
    return None
