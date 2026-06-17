"""Solution for bit_10: Missing Number.

Given an array arr of n distinct integers in
[0, n] (so the array has length n and the values
should be exactly 0, 1, ..., n but one value is
missing), return the missing value. Two clean
solutions: (1) XOR all values with all indices 0..n;
the missing value is left over because every other
value cancels with its index. (2) Compute the
expected sum n*(n+1)/2 and subtract the actual sum.
Both run in O(n) time and O(1) extra space.
Source: https://www.geeksforgeeks.org/find-the-missing-number/

Inputs passed to solve():
    arr: list of n distinct integers in [0, n] with one value missing.
    n: length of arr (so the missing value is in [0, n]).

Goal:
    the missing integer.

Samples:
Sample 1 input:  arr = [3, 0, 1], n = 3
Sample 1 output: 2

Sample 2 input:  arr = [0, 1, 2, 3, 5], n = 5
Sample 2 output: 4

Sample 3 input:  arr = [0], n = 1
Sample 3 output: 1

"""

def solve(arr, n):
    # Write your code here.
    return None
