"""
Description
-----------
Implement the Disjoint Set Union data structure with path
compression and union by rank. ops is a list of tuples:
  ("union", a, b) — union the sets of a and b
  ("find",  a, b) — return True iff a and b are in the same set
Return a list of bools, one per ("find", ...) op, in order.
Requirement: O(α(n)) per op (effectively constant).
Source: https://www.geeksforgeeks.org/union-find/

Examples
--------
Example 1:
Input:  n = 5, ops = [('union', 0, 1), ('find', 0, 1)]
Output: [True]

Example 2:
Input:  n = 4, ops = [('union', 0, 1), ('find', 2, 3)]
Output: [False]

Example 3:
Input:  n = 3, ops = [('union', 0, 1), ('union', 1, 2), ('find', 0, 2)]
Output: [True]
"""

def solve(n, ops):
    # Write your code here.
    return None
