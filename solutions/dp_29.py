"""
Description
-----------
Length of the longest strictly-increasing subsequence.
Patience sort: maintain a sorted tails array;
for each value, binary-search the leftmost position in
tails that's >= the value and place it. The final
length of tails is the LIS length. O(n log n).
Source: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

Examples
--------
Example 1:
Input:  arr = [10, 22, 9, 33, 21, 50, 41, 60, 80], n = 9
Output: 6 (10, 22, 33, 50, 60, 80)

Example 2:
Input:  arr = [3, 1, 4, 1, 5, 9, 2, 6], n = 8
Output: 4 (1, 4, 5, 9)
"""

def solve(arr, n):
    # Write your code here.
    return None
