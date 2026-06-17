"""Solution for fenwick_04: Range Update + Point Query (BIT).


            Maintain an array of n integers under repeated
            range-add updates (add `val` to every element in
            the range [l, r]) and point queries (return the
            current value at index `idx`). The classic BIT
            trick: maintain a single BIT, add `val` at index
            `l` and subtract `val` at index `r+1`. The point
            query at `idx` is then the prefix sum [0, idx].
            O(log n) per update and per query.
            Source: https://www.geeksforgeeks.org/dsa/binary-indexed-tree-range-update-point-query/
            

Inputs passed to solve():
    arr: list of n initial values (informational only).
    n: length of arr.
    range_updates: list of (l, r, val) tuples: add val to arr[l..r].
    point_queries: list of (idx,) tuples to read.
    q: number of point queries.

Goal:
    a list of q point values after all range updates.

Samples:
Sample 1 input:  arr = [0,0,0,0,0], n = 5, range_updates = [(1,3,5)], point_queries = [(0,),(1,),(2,),(3,),(4,)], q = 5
Sample 1 output: [0, 5, 5, 5, 0]

Sample 2 input:  arr = [1,3,5,7], n = 4, range_updates = [(0,2,10),(2,3,-3)], point_queries = [(0,),(1,),(2,),(3,)], q = 4
Sample 2 output: [11, 13, 12, 4]


"""

def solve(arr, n, range_updates, point_queries, q):
    # Write your code here.
    return None
