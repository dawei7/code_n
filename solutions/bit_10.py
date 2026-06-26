"""
Description
-----------
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

Examples
--------
Example 1:
Input:  arr = [3, 0, 1], n = 3
Output: 2

Example 2:
Input:  arr = [0, 1, 2, 3, 5], n = 5
Output: 4

Example 3:
Input:  arr = [0], n = 1
Output: 1
"""

def solve(arr, n):
    # Write your code here.
    return None
