"""Solution for suffix_01: Build Suffix Array.

Return the suffix array of s - a sorted list of
starting indices of every suffix. Naive: build all n
suffixes (as strings) and sort. O(n^2 log n). The
verify just checks the result is a permutation and the
suffixes are non-decreasing.
Source: https://www.geeksforgeeks.org/suffix-array-set-1-introduction/

Inputs passed to solve():
    s: string of n characters.
    n: length of s.

Goal:
    a permutation of [0..n-1] in suffix-sorted order.

Samples:
Sample 1 input:  s = 'banana', n = 6
Sample 1 output: [5, 3, 1, 0, 4, 2] (suffixes a, ana, anana, banana, na, nana)


"""

def solve(s, n):
    # Write your code here.
    return None
