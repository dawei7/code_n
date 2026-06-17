"""Solution for segtree_06: Range Min with Lazy Updates.


            Build a min-segment tree on arr. Apply a sequence
            of range updates (set every element in [l, r] to
            `val`) using lazy propagation (assignment, not
            addition). After all updates, for each query
            (l, r), return the minimum of the current arr
            values in that range. O(log n) per op.
            Source: https://www.geeksforgeeks.org/dsa/lazy-propagation-in-segment-tree-set-2/
            

Inputs passed to solve():
    arr: list of n integers (initial).
    n: length of arr.
    range_updates: list of (l, r, val) tuples: set every arr[i] in [l, r] to val (assignment).
    queries: list of (l, r) range-min queries (after all updates).
    q: number of queries.

Goal:
    a list of q range minimums after all range assignments.

Samples:
Sample 1 input:  arr = [1, 3, 5, 7, 9, 11], n = 6, range_updates = [(1, 3, 5)], queries = [(0, 5)], q = 1
Sample 1 output: [1] (after assignment [1,5,5,5,9,11], min is 1)

Sample 2 input:  arr = [5, 5, 5, 5, 5], n = 5, range_updates = [(1, 3, 0)], queries = [(0, 4)], q = 1
Sample 2 output: [0] (after [5,0,0,0,5], min is 0)


"""

def solve(arr, n, range_updates, queries, q):
    # Write your code here.
    return None
