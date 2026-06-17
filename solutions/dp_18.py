"""Solution for dp_18: Max Product Subarray.

Return the maximum product of a contiguous subarray.
May contain negatives; track BOTH the max-ending-here
and min-ending-here products (a negative * negative
flips the sign and may yield a new max).
Requirement: O(n) — single pass.
Source: https://www.geeksforgeeks.org/maximum-product-subarray/

Inputs passed to solve():
    arr: list of integers (positive, negative, or zero).

Goal:
    the maximum product of any contiguous subarray.

Samples:
Sample 1 input:  arr = [2, 3, -2, 4]
Sample 1 output: 6 (subarray [2, 3])

Sample 2 input:  arr = [-2, 0, -1]
Sample 2 output: 0

Sample 3 input:  arr = [-2, 3, -4]
Sample 3 output: 24 (subarray [-2, 3, -4])

"""

def solve(arr):
    # Write your code here.
    return None
