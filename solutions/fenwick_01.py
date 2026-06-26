"""
Description
-----------
Build a Binary Indexed Tree (Fenwick tree) for arr.
bit[i] = sum of arr[i - 2^k + 1 .. i] where k is the
number of trailing zeros in i. O(n) build. After build,
any prefix sum can be computed in O(log n).
Source: https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

Examples
--------
Example 1:
Input:  arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9], n = 12
Output: [0, 2, 3, 1, 7, 2, 5, 4, 14, 6, 13, 8, 9]
"""

def solve(arr, n):
    # Write your code here.
    return None
