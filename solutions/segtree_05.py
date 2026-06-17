"""Solution for segtree_05: Range Update with Lazy Propagation.


            Build a sum-segment tree, then apply a sequence
            of range updates (add `val` to every element in
            [l, r]) using lazy propagation: when a node is
            fully inside the update range, add `val * width`
            to that node's sum and remember the pending
            update in a parallel `lazy` array (to be pushed
            down only when needed). Then for each query
            (l, r), return the range sum (with lazy tags
            pushed down on the way). O(log n) per op.
            Source: https://www.geeksforgeeks.org/dsa/lazy-propagation-in-segment-tree/
            

Inputs passed to solve():
    arr: list of n integers (initial).
    n: length of arr.
    range_updates: list of (l, r, val) tuples: add val to arr[l..r].
    queries: list of (l, r) range-sum queries (after all updates).
    q: number of queries.

Goal:
    a list of q range sums after all range updates.

Samples:
Sample 1 input:  arr = [1, 3, 5, 7, 9, 11], n = 6, range_updates = [(1, 3, 5)], queries = [(0, 5)], q = 1
Sample 1 output: [46] (= 1+8+10+12+9+11)

Sample 2 input:  arr = [1, 2, 3], n = 3, range_updates = [(0, 2, 10)], queries = [(0, 0), (1, 2), (0, 2)], q = 3
Sample 2 output: [11, 25, 36]


"""

def solve(arr, n, range_updates, queries, q):
    # Write your code here.
    return None
