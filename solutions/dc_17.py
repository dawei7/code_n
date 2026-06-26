"""
Description
-----------
Given an array of n integers, return the minimum
            and maximum values using only (3n/2) - 2 comparisons
            in the worst case. The D&C tournament method: for
            n = 1 the min and max are both the element; for n = 2
            they are decided in one comparison; for larger n,
            recursively solve both halves, then take min of the
            mins and max of the maxes (2 more comparisons).
            Source: https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/

Examples
--------
Example 1:
Input:  arr = [3, 5, 4, 1, 9], n = 5
Output: [1, 9]

Example 2:
Input:  arr = [22, 14, 8, 17, 35, 3], n = 6
Output: [3, 35]

Example 3:
Input:  arr = [7], n = 1
Output: [7, 7]

Example 4:
Input:  arr = [2, 1], n = 2
Output: [1, 2]
"""

def solve(arr, n):
    # Write your code here.
    return None
