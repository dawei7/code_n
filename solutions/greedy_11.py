"""
Description
-----------
Represent a rational number p/q (with p, q > 0) as a sum of
distinct unit fractions 1/d_i. The greedy algorithm picks
the smallest unit fraction >= p/q at each step, which is
1 / ceil(q/p), and recurses on the remainder.
Requirement: O(q) iterations in the worst case.
Source: https://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-algorithm/

Examples
--------
Example 1:
Input:  p = 2, q = 3
Output: [2, 6]  (2/3 = 1/2 + 1/6)

Example 2:
Input:  p = 6, q = 14
Output: [3, 11, 231]  (6/14 = 1/3 + 1/11 + 1/231)

Example 3:
Input:  p = 1, q = 2
Output: [2]
"""

def solve(p, q):
    # Write your code here.
    return None
