"""Solution for graph_09: Union-Find (DSU).

Implement the Disjoint Set Union data structure with path
compression and union by rank. ops is a list of tuples:
  ("union", a, b) — union the sets of a and b
  ("find",  a, b) — return True iff a and b are in the same set
Return a list of bools, one per ("find", ...) op, in order.
Requirement: O(α(n)) per op (effectively constant).
Source: https://www.geeksforgeeks.org/union-find/

Inputs passed to solve():
    n: number of elements (0 to n-1).
    ops: list of operation tuples: ("union", a, b) or ("find", a, b).

Goal:
    a list of bools (one per "find" op) — True iff the two elements share a set.

Samples:
Sample 1 input:  n = 5, ops = [('union', 0, 1), ('find', 0, 1)]
Sample 1 output: [True]

Sample 2 input:  n = 4, ops = [('union', 0, 1), ('find', 2, 3)]
Sample 2 output: [False]

Sample 3 input:  n = 3, ops = [('union', 0, 1), ('union', 1, 2), ('find', 0, 2)]
Sample 3 output: [True]

"""

def solve(n, ops):
    # Write your code here.
    return None
