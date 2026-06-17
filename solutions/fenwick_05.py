"""Solution for fenwick_05: Range Update + Range Query (BIT).


            Maintain an array of n integers under repeated
            range-add updates and range-sum queries. Use two
            BITs: BIT1 holds a difference array; BIT2 holds a
            second auxiliary array. After a range update (l,
            r, val), update BIT1 with (l, +val, r+1, -val)
            and BIT2 with (l, val*(l-1), r+1, -val*r). The
            range sum [0, x] = prefix_BIT1(x) * x - prefix_BIT2(x).
            Then range sum [l, r] = sum(r) - sum(l-1). O(log n)
            per update and per query.
            Source: https://www.geeksforgeeks.org/dsa/binary-indexed-tree-range-update-range-queries/
            

Inputs passed to solve():
    arr: list of n initial values (informational only).
    n: length of arr.
    range_updates: list of (l, r, val) tuples: add val to arr[l..r].
    range_queries: list of (l, r) tuples to read.
    q: number of range queries.

Goal:
    a list of q range sums after all range updates.

Samples:
Sample 1 input:  arr = [0,0,0,0,0], n = 5, range_updates = [(1,3,2)], range_queries = [(0,4),(0,0),(1,3)], q = 3
Sample 1 output: [6, 0, 6]


"""

def solve(arr, n, range_updates, range_queries, q):
    # Write your code here.
    return None
