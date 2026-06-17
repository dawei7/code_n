"""Solution for segtree_04: Range Minimum Query.


            Build a min-segment tree on arr (each node stores
            the minimum of its sub-range). For each query
            (l, r), descend into the tree collecting the
            minimums that exactly tile [l, r]. Return the
            list of q range minimums. O(log n) per query.
            Source: https://www.geeksforgeeks.org/dsa/segment-tree-range-minimum-query/
            

Inputs passed to solve():
    arr: list of n integers.
    n: length of arr.
    queries: list of (l, r) tuples.
    q: number of queries.

Goal:
    a list of q range minimums.

Samples:
Sample 1 input:  arr = [1, 3, 5, 7, 9, 11], n = 6, queries = [(1, 3), (0, 5)], q = 2
Sample 1 output: [3, 1]

Sample 2 input:  arr = [5, 2, 8, 1, 9, 3], n = 6, queries = [(0, 2), (3, 5)], q = 2
Sample 2 output: [2, 1]


"""

def solve(arr, n, queries, q):
    # Write your code here.
    return None
