"""Solution for fenwick_01: Build Fenwick Tree.

Build a Binary Indexed Tree (Fenwick tree) for arr.
bit[i] = sum of arr[i - 2^k + 1 .. i] where k is the
number of trailing zeros in i. O(n) build. After build,
any prefix sum can be computed in O(log n).
Source: https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

Inputs passed to solve():
    arr: list of n integers.
    n: length of arr.

Goal:
    a list of length n+1 representing the BIT (1-indexed).

Samples:
Sample 1 input:  arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9], n = 12
Sample 1 output: [0, 2, 3, 1, 7, 2, 5, 4, 14, 6, 13, 8, 9]


"""

def solve(arr, n):
    # Write your code here.
    return None
