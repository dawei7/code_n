"""
Description
-----------
Build a sum-segment tree from arr and return it as a
flat list. The tree has 4*n slots: tree[1] is the root,
tree[2k] / tree[2k+1] are the left/right children.
Leaves at positions n..2n-1 hold arr[i - n]. Each
internal node holds the sum of its two children. O(n).
Source: https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/

Examples
--------
Example 1:
Input:  arr = [1, 3, 5, 7, 9, 11], n = 6
Output: [..., 36, ..., arr leaves ..., internal nodes ...]
"""

def solve(arr, n):
    # Write your code here.
    return None
