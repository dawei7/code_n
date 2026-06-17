"""Solution for segtree_02: Range Sum Query.

Build a segment tree, then return the range-sum for
each (l, r) query. Standard divide-and-conquer query:
if the node's range is fully inside [l, r], return the
node's value; if outside, return 0; otherwise recurse.
O(log n) per query.
Source: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/

Inputs passed to solve():
    arr: list of n integers.
    n: length of arr.
    queries: list of (l, r) tuples.
    q: number of queries.

Goal:
    a list of q range sums.

Samples:
Sample 1 input:  arr = [1, 3, 5, 7, 9, 11], n = 6, queries = [(1, 3), (0, 5)], q = 2
Sample 1 output: [15, 36]


"""

def solve(arr, n, queries, q):
    # Write your code here.
    return None
