"""Solution for segtree_03: Point Update.

Apply a sequence of point updates (idx, val) to arr
(arr[idx] = val for each) and return the final array.
In a real segment tree, an update would also recompute
all ancestors in O(log n); this spec asks for the
resulting array, which is the contract the verifier
expects.
Source: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/

Inputs passed to solve():
    arr: list of n integers (initial).
    n: length of arr.
    updates: list of (idx, val) tuples to apply.
    q: number of updates.

Goal:
    the array after applying all updates.

Samples:
Sample 1 input:  arr = [1, 3, 5, 7, 9, 11], n = 6, updates = [(1, 10), (3, 20)], q = 2
Sample 1 output: [1, 10, 5, 20, 9, 11]


"""

def solve(arr, n, updates, q):
    # Write your code here.
    return None
