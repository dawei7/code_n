"""Solution for segtree_01: Build Segment Tree.

Build a sum-segment tree from arr and return it as a
flat list. The tree has 4*n slots: tree[1] is the root,
tree[2k] / tree[2k+1] are the left/right children.
Leaves at positions n..2n-1 hold arr[i - n]. Each
internal node holds the sum of its two children. O(n).
Source: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/

Inputs passed to solve():
    arr: list of n integers.
    n: length of arr.

Goal:
    a flat list of length 4*n representing the sum segment tree.

Samples:
Sample 1 input:  arr = [1, 3, 5, 7, 9, 11], n = 6
Sample 1 output: [..., 36, ..., arr leaves ..., internal nodes ...]


"""

def solve(arr, n):
    # Write your code here.
    return None
