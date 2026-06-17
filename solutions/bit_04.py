"""Solution for bit_04: Power Set.

Return every subset of the input list as a list
of lists. The number of subsets is 2^n; for each
mask in [0, 2^n), include arr[i] iff bit i of mask
is set. O(2^n * n) time.
Source: https://www.geeksforgeeks.org/power-set/

Inputs passed to solve():
    arr: list of n distinct integers (capped at 6 in the setup).
    n: length of arr.

Goal:
    a list of 2^n subsets (each a list), in bit-iteration order.

Samples:
Sample 1 input:  arr = [1, 2, 3], n = 3
Sample 1 output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Sample 2 input:  arr = [1], n = 1
Sample 2 output: [[], [1]]


"""

def solve(arr, n):
    # Write your code here.
    return None
