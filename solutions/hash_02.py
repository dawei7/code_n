"""
Description
-----------
Count the number of contiguous subarrays whose sum equals k.
Trick: the number of subarrays ending at i with sum k equals the
number of earlier prefix sums equal to prefix[i] - k. Hash the
prefix-sum counts. O(n).
Source: https://www.geeksforgeeks.org/number-subarrays-sum-exactly-k/

Examples
--------
Example 1:
Input:  arr = [1, 1, 1], k = 2, n = 3
Output: 2 (1+1, 1+1)

Example 2:
Input:  arr = [1, 2, 3], k = 3, n = 3
Output: 2 (1+2, 3)
"""

def solve(arr, k, n):
    # Write your code here.
    return None
