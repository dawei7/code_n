"""Solution for fenwick_02: Range Sum Query (BIT).

Build a BIT, apply a sequence of point updates, then
answer each range-sum query by summing prefix sums.
O(log n) per update and per query.
Source: https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

Inputs passed to solve():
    arr: list of n integers (initial).
    n: length of arr.
    updates: list of (idx, val) tuples (set arr[idx] = val).
    queries: list of (l, r) tuples (range sums).
    q: number of queries.

Goal:
    a list of q range sums after applying the updates.

Samples:
Sample 1 input:  arr = [1, 3, 5], n = 3, updates = [(1, 8)], queries = [(0, 2)], q = 1
Sample 1 output: [12]


"""

def solve(arr, n, updates, queries, q):
    # Write your code here.
    return None
